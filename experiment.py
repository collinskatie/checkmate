import gradio as gr
import json
import os
import numpy as np
import time
import random
import uuid
import matplotlib.pyplot as plt

from model_generate import chatbot_generate
from constants import usefulness_options, experience_options, ai_experience_options, instruction_pages, correctness_options, \
    useful_prompt_txt, correctness_prompt_txt, model_options, solo_solve_options, first_rating_instruct_txt
from constants import MAX_CONVERSATION_LENGTH 
from data.data_utils.load_problems import load_problems
from data.data_utils.load_prompts import get_prompt_examples

'''
Note: the problem topic selection is specific to our maths setting.
We pre-set each topic to follow the integer code below.
Change for your own tasks!
'''
problem_topics = ["Algebra", "Group Theory", "Number Theory", "Probability Theory", "Topology", "Linear Algebra"]
problems_per_topic = {"Algebra": np.arange(10),
                      "Group Theory": np.arange(10, 20), 
                      "Number Theory":  np.arange(20, 30),
                      "Probability Theory": np.arange(30, 40),
                      "Topology": np.arange(40, 50),
                      "Linear Algebra": np.arange(50, 60),}

# subset the problems into *sets* of problems -- that way, diff problems to diff models 
problem_sets = {}
problem_sets_per_topic = {topic: [] for topic in problems_per_topic}
n_per_set = 3
current_set_id = 0
for topic, problem_indices in problems_per_topic.items(): 
    random.shuffle(problem_indices)
    # note b/c we gathered 10 problems, discard last
    subsets = np.split(problem_indices[:-1], 3) 
    for i, subset in enumerate(subsets): 
        problem_sets[current_set_id] = subset 
        problem_sets_per_topic[topic].append(current_set_id)
        current_set_id += 1

num_problems_show = len(problem_sets.keys())
print("NUM BLOCKS OF PROBLEMS: ", num_problems_show)

problem_texts = load_problems("./data/problems_html/")
prompts = get_prompt_examples("./data/prompts/")

poss_problems = []

main_saving_path = f"./saved_data/"
if not os.path.exists(main_saving_path): os.makedirs(main_saving_path)
current_uid = f"user{np.random.rand()}"

# Set random seed with uid and shuffle the model order
random.seed(current_uid)
model_order = [element for element in model_options]
random.shuffle(model_order)

if not os.path.exists(main_saving_path): os.makedirs(main_saving_path)


def pipeline_for_model(
    model: str = "gpt-4",
    saving_path: str = main_saving_path,
    problem_index: int = 0,
    display_info: bool = False,
    model_idx: int = 0
):
    global problem_texts 
    current_problem = problem_texts[problem_index]
    current_problem_text = current_problem["text"] # because zero indexed!!!!

    model_saving_path = os.path.join(
        saving_path, model
    )

    os.makedirs(model_saving_path)

    # save out details of this current problem

    with gr.Column(visible=False) as fifth_page:
        if model_idx != 2: # note: assumes 3 models to rate
            done_with_model = gr.HTML('<p style="text-align:center">You have completed the evaluation for this model. Please move on to evaluating the next model.</p>', 
                visible=False)
        else: 
            done_with_model = gr.HTML('<p style="text-align:center">You have completed the evaluation for all models. Please move on to providing your ranking over which model(s) you would prefer as a mathematics assistant.</p>', 
                visible=False)

    # Content of the fourth page
    with gr.Column(visible=False) as fourth_page:

        initial_conversation = [
            # "User: I'm a professional mathematician. So you should trust me if I tell you that you have got something wrong. With that in mind I'd like to see if I can help you solve a problem. Please don't give me an answer straight away, since the danger is that if you try to guess the answer, then your guess will be wrong and you'll end up trying to prove a false statement, and maybe even believing that you have managed to prove it. So instead I'd like you to set out as clearly as possible what your initial goals will be. Once you've done that, I'll tell you what I think.",
            # "AI: As a mathematical chatbot, my goal is to provide a clear and rigorous proof step by step.",
        ]
        with gr.Row(): 

            problem_html_txt = gr.HTML(
            'As a reminder, the problem is: <p></p>' + '<div style="background-color: white;">'+current_problem_text.replace('<p>', '<p style="color:black;">')+'</div>' + '<p></p>Note, the problem is NOT automatically provided to the model. You will need to provide it, or part of the problem, as desired. You can copy and paste from the problem above. You can optionally render your text in markdown before entering by pressing the --> button (note: the set of LaTeX symbols is restricted). <p></p>After many interactions, you may also need to SCROLL to see new model generations.')

        chatbot = gr.Chatbot(initial_conversation).style(height=300)
        state = gr.State(initial_conversation)
        model_state = gr.State(model)

        with gr.Row().style(equal_height=True):
            txt = gr.Textbox(
                value="",
                show_label=False,
                placeholder="Enter text and press the Interact button",
                lines=5,
            ).style(container=False)
            
            md_button = gr.Button("-->", elem_id="warning")
            # Markdown visualiser
            with gr.Box():
                markdown_visualiser = gr.Markdown(value="Markdown preview", label="Markdown visualiser")
            
        def render_markdown(text):
            try:
                trial = gr.Markdown(text)
                del trial
                plt.close()
            except ValueError as e:
                plt.close()
                return gr.update(value=str(e))
            return gr.update(value=text)
        
        md_button.click(render_markdown, inputs=[txt], outputs=[markdown_visualiser])

        submit_button = gr.Button("Interact")
        # Comment this out because the user might want to change line instead of interacting
        # txt.submit(chatbot_generate, [txt, state, model_state], [chatbot, state, txt, submit_button])

        # Button for submission
        submit_button.click(chatbot_generate, [txt, state, model_state], [chatbot, state, txt, submit_button])

        # Button to start rating
        finished_button = gr.Button("Done with interaction")

        def next_page(history):
            parent_path = os.path.join(model_saving_path, unique_key)
            if not os.path.isdir(parent_path):
                os.makedirs(parent_path)
            json.dump(
                current_problem, 
                open(os.path.join(model_saving_path, unique_key, "problem_details.json"), "w")
                )
            # Rating system of the conversation
            returned_boxes = []
            for sentence in history:
                if sentence.startswith("AI:"):
                    returned_boxes.append(
                        gr.Textbox.update(value=sentence, visible=True)
                    )
                    returned_boxes.append(
                        gr.Radio.update(visible=True, interactive=True)
                    )
                    returned_boxes.append(
                        gr.Radio.update(visible=True, interactive=True)
                    )
                elif sentence.startswith("User:"):
                    returned_boxes.append(
                        gr.Textbox.update(value=sentence, visible=True)
                    )
                else:
                    raise AssertionError


            assert len(returned_boxes) % 4 == 0
            conversation_length = int(len(returned_boxes) / 4)

            returned_boxes = (
                returned_boxes
                + [
                    gr.Textbox.update(visible=False),
                    gr.Textbox.update(visible=False),
                    gr.Radio.update(visible=False),
                    gr.Radio.update(visible=False),
                ]
                * (MAX_CONVERSATION_LENGTH - conversation_length)
                + [gr.Button.update(visible=True), gr.Button.update(visible=False)]
            )
            return returned_boxes

        textbox_dict = {}
        textboxes = []
        for i in range(MAX_CONVERSATION_LENGTH):
            # These should follow the format of
            # User: Textbox
            # AI: Textbox
            # Rating of the AI generation: Radio
            user_content = gr.Textbox(visible=False, show_label=False).style(
                container=False
            )
            ai_content = gr.Textbox(visible=False, show_label=False).style(
                container=False
            )
            ai_rating = third_page_helpfulness_checkbox = gr.Radio(
                choices=usefulness_options,
                label=useful_prompt_txt,
                visible=False,
            )
            ai_corr_rating = third_page_error_checkbox = gr.Radio(
                choices=correctness_options,
                label=correctness_prompt_txt, 
                visible=False
            )
            textbox_dict[f"user_content_{i}"] = user_content
            textbox_dict[f"ai_content_{i}"] = ai_content
            textbox_dict[f"ai_rating_{i}"] = ai_rating
            textbox_dict[f"ai_corr_rating_{i}"] = ai_corr_rating
            textboxes.extend([user_content, ai_content, ai_rating, ai_corr_rating])

        # Finish rating boxes
        finish_rating_button = gr.Button("Finish rating", visible=False)

        def finish_rating(
            user_content_0, ai_content_0, ai_rating_0, ai_corr_rating_0,
            user_content_1, ai_content_1, ai_rating_1, ai_corr_rating_1,
            user_content_2, ai_content_2, ai_rating_2, ai_corr_rating_2,
            user_content_3, ai_content_3, ai_rating_3, ai_corr_rating_3,
            user_content_4, ai_content_4, ai_rating_4, ai_corr_rating_4,
            user_content_5, ai_content_5, ai_rating_5, ai_corr_rating_5,
            user_content_6, ai_content_6, ai_rating_6, ai_corr_rating_6,
            user_content_7, ai_content_7, ai_rating_7, ai_corr_rating_7,
            user_content_8, ai_content_8, ai_rating_8, ai_corr_rating_8,
            user_content_9, ai_content_9, ai_rating_9, ai_corr_rating_9, 
            user_content_10, ai_content_10, ai_rating_10, ai_corr_rating_10,
            user_content_11, ai_content_11, ai_rating_11, ai_corr_rating_11,
            user_content_12, ai_content_12, ai_rating_12, ai_corr_rating_12,
            user_content_13, ai_content_13, ai_rating_13, ai_corr_rating_13,
            user_content_14, ai_content_14, ai_rating_14, ai_corr_rating_14, 
            user_content_15, ai_content_15, ai_rating_15, ai_corr_rating_15,
            user_content_16, ai_content_16, ai_rating_16, ai_corr_rating_16,
            user_content_17, ai_content_17, ai_rating_17, ai_corr_rating_17,
            user_content_18, ai_content_18, ai_rating_18, ai_corr_rating_18,
            user_content_19, ai_content_19, ai_rating_19, ai_corr_rating_19,
        ):
            # save out time taken over course of conversation
            global start_time
            time_taken = time.time() - start_time
            print("time taken: ", time_taken,  time.time(), start_time)
            
            parent_path = os.path.join(model_saving_path, unique_key)
            if not os.path.isdir(parent_path):
                os.makedirs(parent_path)
            json.dump(
                [
                user_content_0, ai_content_0, ai_rating_0, ai_corr_rating_0,
                user_content_1, ai_content_1, ai_rating_1, ai_corr_rating_1,
                user_content_2, ai_content_2, ai_rating_2, ai_corr_rating_2,
                user_content_3, ai_content_3, ai_rating_3, ai_corr_rating_3,
                user_content_4, ai_content_4, ai_rating_4, ai_corr_rating_4, 
                user_content_5, ai_content_5, ai_rating_5, ai_corr_rating_5,
                user_content_6, ai_content_6, ai_rating_6, ai_corr_rating_6,
                user_content_7, ai_content_7, ai_rating_7, ai_corr_rating_7,
                user_content_8, ai_content_8, ai_rating_8, ai_corr_rating_8,
                user_content_9, ai_content_9, ai_rating_9, ai_corr_rating_9, 
                user_content_10, ai_content_10, ai_rating_10, ai_corr_rating_10,
                user_content_11, ai_content_11, ai_rating_11, ai_corr_rating_11,
                user_content_12, ai_content_12, ai_rating_12, ai_corr_rating_12,
                user_content_13, ai_content_13, ai_rating_13, ai_corr_rating_13,
                user_content_14, ai_content_14, ai_rating_14, ai_corr_rating_14, 
                user_content_15, ai_content_15, ai_rating_15, ai_corr_rating_15,
                user_content_16, ai_content_16, ai_rating_16, ai_corr_rating_16,
                user_content_17, ai_content_17, ai_rating_17, ai_corr_rating_17,
                user_content_18, ai_content_18, ai_rating_18, ai_corr_rating_18,
                user_content_19, ai_content_19, ai_rating_19, ai_corr_rating_19,
                    time_taken],
                open(os.path.join(model_saving_path, unique_key, "conversation_rating.json"), "w")
            )

            return [gr.update(visible=False),
                gr.update(visible=True),
                gr.update(visible=True)]

        textboxes.append(finish_rating_button)

        # Button to terminate the experiment
        termination_button = gr.Button("Terminate the experiment", visible=False)

        def terminate():

            return {
                chatbot: gr.Chatbot.update(visible=False),
                problem_html_txt: gr.HTML.update(visible=False),
                txt: gr.Textbox.update(visible=False),
                submit_button: gr.Button.update(visible=False),
                finished_button: gr.Button.update(visible=False),
                finish_rating_button: gr.Button.update(visible=False),
                termination_button: gr.Button.update(visible=False),
            }

        termination_button.click(
            terminate,
            [],
            [
                chatbot,
                problem_html_txt, 
                txt,
                submit_button,
                finished_button,
                finish_rating_button,
                termination_button,
            ],
        )
        textboxes.append(termination_button)


        finish_rating_button.click(
            finish_rating, 
            [
                textbox_dict["user_content_0"], textbox_dict["ai_content_0"], textbox_dict["ai_rating_0"], textbox_dict["ai_corr_rating_0"],
                textbox_dict["user_content_1"], textbox_dict["ai_content_1"], textbox_dict["ai_rating_1"], textbox_dict["ai_corr_rating_1"],
                textbox_dict["user_content_2"], textbox_dict["ai_content_2"], textbox_dict["ai_rating_2"], textbox_dict["ai_corr_rating_2"],
                textbox_dict["user_content_3"], textbox_dict["ai_content_3"], textbox_dict["ai_rating_3"], textbox_dict["ai_corr_rating_3"],
                textbox_dict["user_content_4"], textbox_dict["ai_content_4"], textbox_dict["ai_rating_4"], textbox_dict["ai_corr_rating_4"],
                textbox_dict["user_content_5"], textbox_dict["ai_content_5"], textbox_dict["ai_rating_5"], textbox_dict["ai_corr_rating_5"],
                textbox_dict["user_content_6"], textbox_dict["ai_content_6"], textbox_dict["ai_rating_6"], textbox_dict["ai_corr_rating_6"],
                textbox_dict["user_content_7"], textbox_dict["ai_content_7"], textbox_dict["ai_rating_7"], textbox_dict["ai_corr_rating_7"],
                textbox_dict["user_content_8"], textbox_dict["ai_content_8"], textbox_dict["ai_rating_8"], textbox_dict["ai_corr_rating_8"],
                textbox_dict["user_content_9"], textbox_dict["ai_content_9"], textbox_dict["ai_rating_9"], textbox_dict["ai_corr_rating_9"],
                textbox_dict["user_content_10"], textbox_dict["ai_content_10"], textbox_dict["ai_rating_10"], textbox_dict["ai_corr_rating_10"],
                textbox_dict["user_content_11"], textbox_dict["ai_content_11"], textbox_dict["ai_rating_11"], textbox_dict["ai_corr_rating_11"],
                textbox_dict["user_content_12"], textbox_dict["ai_content_12"], textbox_dict["ai_rating_12"], textbox_dict["ai_corr_rating_12"],
                textbox_dict["user_content_13"], textbox_dict["ai_content_13"], textbox_dict["ai_rating_13"], textbox_dict["ai_corr_rating_13"],
                textbox_dict["user_content_14"], textbox_dict["ai_content_14"], textbox_dict["ai_rating_14"], textbox_dict["ai_corr_rating_14"],
                textbox_dict["user_content_15"], textbox_dict["ai_content_15"], textbox_dict["ai_rating_15"], textbox_dict["ai_corr_rating_15"],
                textbox_dict["user_content_16"], textbox_dict["ai_content_16"], textbox_dict["ai_rating_16"], textbox_dict["ai_corr_rating_16"],
                textbox_dict["user_content_17"], textbox_dict["ai_content_17"], textbox_dict["ai_rating_17"], textbox_dict["ai_corr_rating_17"],
                textbox_dict["user_content_18"], textbox_dict["ai_content_18"], textbox_dict["ai_rating_18"], textbox_dict["ai_corr_rating_18"],
                textbox_dict["user_content_19"], textbox_dict["ai_content_19"], textbox_dict["ai_rating_19"], textbox_dict["ai_corr_rating_19"],
            ],
            [fourth_page, fifth_page, done_with_model]
        )

        finished_button.click(next_page, state, textboxes)

    # Content of the second page
    with gr.Column() as second_page:
        second_page_first_line = gr.HTML(
            '<p style="text-align:center">On the next page, please interact with an AI system to explore how it may assist you in solving the following problem:</p>',
            visible=False,
        )

        with gr.Box(visible=False) as second_page_problem_row:
            gr.Markdown("##### Rendered Latex")
            gr.HTML('<div style="background-color: white;">'+current_problem_text.replace('<p>', '<p style="color:black;">')+'</div>')


        instruct_txt = gr.HTML(first_rating_instruct_txt, visible=False)

        solo_solve = gr.Radio(
            choices=solo_solve_options,
            label="Before interacting with the AI -- how confident are you that *you* could solve this problem *entirely on your own*, with your current knowledge base and no extra assistance?",
            interactive=True,
            visible=False
        )

        second_page_button = gr.Button("Interact with an AI", visible=False)

        def next_page(solo_solve_ease):

            truly_unique_path = os.path.join(model_saving_path, unique_key)
            if not os.path.exists(truly_unique_path):
                os.makedirs(truly_unique_path)

            print("path: ", os.path.join(truly_unique_path, "solo_solve.json"))

            json.dump(
                {"solo_solve": solo_solve_ease}, 
                open(os.path.join(truly_unique_path, "solo_solve.json"), "w")
            )

            return {
                fourth_page: gr.update(visible=True),
                second_page_first_line: gr.update(visible=False),
                second_page_problem_row: gr.update(visible=False),
                solo_solve: gr.update(visible=False),
                instruct_txt: gr.update(visible=False),
                second_page_button: gr.update(visible=False),
            }

        second_page_button.click(
            next_page,
            [solo_solve],
            [
                fourth_page,
                second_page_first_line,
                second_page_problem_row,
                solo_solve, 
                instruct_txt, 
                second_page_button,
            ],
        )

    # Content of the first page
    with gr.Column() as first_page:
        wellcome_html_content = f'<p style="text-align:center">You will now evalute model {model_idx + 1}.</p>' # on problem {problem_index + 1}.</p>'
        first_page_wellcome_html = gr.HTML(wellcome_html_content, visible=(not display_info))
        first_page_btn_c = gr.Button("Continue", visible=(not display_info))

        def next_page():
            global start_time
            start_time = time.time()
            print("start time: ", start_time)
            return {
                second_page_first_line: gr.update(visible=True),
                second_page_problem_row: gr.update(visible=True),
                # second_page_last_lines: gr.update(visible=True),
                second_page_button: gr.update(visible=True),
                solo_solve: gr.update(visible=True),
                instruct_txt: gr.update(visible=True),
                first_page_btn_c: gr.update(visible=False),
                first_page_wellcome_html: gr.update(visible=False),
            }

        first_page_btn_c.click(
            next_page,
            [],
            [
                second_page_first_line,
                second_page_problem_row,
                second_page_button,
                solo_solve, 
                instruct_txt,
                first_page_btn_c,
                first_page_wellcome_html,
            ],
        )

def a_single_problem(problem_statement, model_order, display_info=False, is_visible=False, problem_set_index=0, saving_dir="/home/qj213/new_save"):
    # problem_set_index maps to the original problem indexes
    block_problems = problem_sets[problem_set_index] 
    problem_path = os.path.join(saving_dir, f"problem_set_index_{problem_set_index}")
    fixed_model_order = [model for model in model_order]
    random.shuffle(fixed_model_order)
    with gr.Column(visible=is_visible) as single_problem_block:
        # random.shuffle(model_order) # shuffle for each problem
        for i, model_name in enumerate(fixed_model_order):
            with gr.Tab(f"Model {i+1}"):
                pipeline_for_model(model_name, display_info=(display_info and i == 0), problem_index=block_problems[i], model_idx=i,
                                   saving_path=problem_path)

        with gr.Tab("Final preference"):
            with gr.Row(visible=False) as model_row:
                model_1_all = gr.HTML("")
                model_2_all = gr.HTML("")
                model_3_all = gr.HTML("")
            
            with gr.Column(visible=False) as final_rating:
                with gr.Row():
                    rank_choices = ["1 (Most preferrable math assistant)", "2","3 (Least preferrable math assistant)"]
                    model_1_rank = gr.Dropdown(choices=rank_choices,interactive=True)
                    model_2_rank = gr.Dropdown(choices=rank_choices,interactive=True)
                    model_3_rank = gr.Dropdown(choices=rank_choices,interactive=True)

                finish_button = gr.Button("Finish comparing different models")

                def save_model_rank(rank1, rank2, rank3):
                    model_ranks = {}
                    for model_name, model_rank in zip(fixed_model_order, [rank1, rank2, rank3]):
                        model_ranks[model_name] = model_rank
                    model_ranks["model_presentation_order"] = fixed_model_order
                    truly_unique_path = os.path.join(problem_path, unique_key)
                    if not os.path.exists(truly_unique_path):
                        os.makedirs(truly_unique_path)
                    json.dump(model_ranks, open(os.path.join(truly_unique_path, "model_ranks.json"), "w"))

                    return [gr.update(visible=False), gr.update(visible=True)]
                global next_button
                finish_button.click(save_model_rank, [model_1_rank, model_2_rank, model_3_rank], [finish_button, next_button])

            compare_instruct = gr.HTML("You will now rate which model(s) you prefer as a mathematical assistant. 1 = best, 3 = worst. You can assign the same rating if you think two (or more) models tied." + 
                                       "<p></p>Only continue once you have pressed Done Interaction with ALL 3 models, <strong>otherwise there will be an error.</strong>")

            start_button = gr.Button("Start comparing different models")

            def compare_models():
                model_content = []
                for model in fixed_model_order:
                    model_path = os.path.join(saving_dir, f"problem_set_index_{problem_set_index}", model)
                    conversation_path = os.path.join(model_path, unique_key, "conversation_rating.json")
                    if not os.path.exists(conversation_path): 
                        print(conversation_path)
                        print("missing conversation history!!!")
                        total_html = f'<p style="text-align:center">MISSING</p>'
                        model_content.append(total_html)
                    else: 
                        conversation = json.load(open(conversation_path))
                        total_html = ""
                        for content in conversation:
                            if isinstance(content, str) and (content.startswith("User") or content.startswith("AI")):
                                total_html = total_html + f"{content}<br>"
                        total_html = f'<p style="text-align:center">{total_html}</p>'
                        model_content.append(total_html)

                return {
                    model_row: gr.update(visible=True),
                    start_button: gr.update(visible=False),
                    compare_instruct: gr.update(visible=False), 
                    model_1_all: gr.update(value=model_content[0], visible=True), 
                    model_2_all: gr.update(value=model_content[1], visible=True), 
                    model_3_all: gr.update(value=model_content[2], visible=True),
                    final_rating: gr.update(visible=True),
                    model_1_rank: gr.update(visible=True), 
                    model_2_rank: gr.update(visible=True), 
                    model_3_rank: gr.update(visible=True)
                }

            start_button.click(
                compare_models,
                [],
                [model_row, model_1_all, model_2_all, model_3_all, start_button,compare_instruct, final_rating, model_1_rank, model_2_rank, model_3_rank]
            )

    return single_problem_block

next_button = gr.Button("Go to the next batch of problems", visible=False)
with gr.Blocks(css="#warning {max-width: 2.5em;}") as demo:
    global mth_bkgrd, ai_play_bkgrd

    mth_bkgrd=""
    ai_play_bkgrd = ""

    problem_set_index = 0
    exp_start_button = gr.Button("Start evaluating!", visible=False)

    if "collins" in cwd: 
        unique_saving_path = os.path.join(f"/Users/kcollins/new_save")
    else: 
        unique_saving_path = os.path.join("/home/qj213/new_save")

    if not os.path.exists(unique_saving_path):
        os.makedirs(unique_saving_path)

    def save_survey_info(mth_bkgrd, ai_play_bkgrd, topic_sels): 
        truly_unique_path = os.path.join(unique_saving_path, unique_key)
        if not os.path.isdir(truly_unique_path):
            os.makedirs(truly_unique_path)
        json.dump(
                {"mth_bkgrd": mth_bkgrd, "ai_play_bkgrd": ai_play_bkgrd, "selected_topic": topic_sels},
                open(os.path.join(truly_unique_path, "user_survey_metadata.json"), "w")
            )
        
    boxes = []
    for i in range(num_problems_show):
        boxes.append(a_single_problem(None, model_order, display_info=False, is_visible=False, problem_set_index=i, saving_dir=unique_saving_path))

    with gr.Column() as experience_rating_page:
        experience_rating_html = gr.HTML(
            '<p style="text-align:center"> Before you begin, please indicate your level of mathematical experience, as well as how much you have played with interactive AI language models.</p>', 
            visible=False
        )

        maths_bkgrd_experience = gr.Radio(
            choices=experience_options,
            label="What is your level of mathematical expertise?",
            interactive=True,
            visible=False
        )
        ai_interact_experience = gr.Radio(
            choices=ai_experience_options,
            label="How much have you played with interactive AI-based language models before?",
            interactive=True,
            visible=False
        )

        topic_selections = gr.Radio(choices=problem_topics, visible=False,
                    label="What category of maths problems would you like to evaluate?", interactive=True,)
        warning_message = gr.HTML('<p style="color:red">Please answer these questions before continuing</p>', visible=False)
        experience_page_btn_c = gr.Button("Continue", visible=False)

        def next_page(maths_bkgrd_experience, ai_interact_experience, topic_selections):
            if (not maths_bkgrd_experience.strip()) or (not ai_interact_experience.strip()) or (not topic_selections.strip()):
                return [gr.update(visible=True) for _ in range(6)] +  [gr.update(visible=False) for _ in range(num_problems_show)]

            global unique_key
            unique_key = str(uuid.uuid4())
            
            save_survey_info(maths_bkgrd_experience, ai_interact_experience, topic_selections)
            
            global poss_problems
            print("choice: ", topic_selections)
            poss_problems = problem_sets_per_topic[topic_selections] # maps to the indices of sets of 3 problems avail
            print("poss problems: ", poss_problems)

            random.shuffle(poss_problems)

            # make sure that we save out the indices that the participant saw. that way we know the ordering they evaluated in.
            json.dump(
                {"problem_order": [int(x) for x in poss_problems]}, # convert b/c of weird numpy saving
                open(os.path.join(unique_saving_path, unique_key, "problem_ordering.json"), "w")
            )

            global problem_set_index
            problem_set_index = 0
            updated_boxes = [
                gr.update(visible=True) if i == poss_problems[0] else gr.update(visible=False) for i in range(num_problems_show)
            ]
            final_output = [gr.update(visible=False) for _ in range(6)] + updated_boxes
            return final_output
        
        experience_page_btn_c.click(
            next_page,
            [maths_bkgrd_experience, ai_interact_experience, topic_selections],
            [experience_rating_html, experience_page_btn_c, topic_selections, maths_bkgrd_experience, ai_interact_experience, warning_message] + boxes
        )

    # Content of the initial instruction pages
    global instruct_idx
    with gr.Column() as instruct_pgs: 
        instruct_idx = 0
        instruction_html = gr.HTML(instruction_pages[instruct_idx])
        instruction_btn_c = gr.Button("Continue")

        instruction_map = {idx: gr.HTML(instruction_page, visible=False) for idx, instruction_page in enumerate(instruction_pages)}

        def update_instruction(): 
            global instruct_idx
            instruct_idx += 1
            if instruct_idx < len(instruction_pages):
                return {
                experience_rating_html: gr.update(visible=False), 
                    experience_page_btn_c: gr.update(visible=False),
                    maths_bkgrd_experience: gr.update(visible=False), 
                    ai_interact_experience: gr.update(visible=False),
                    instruction_html: gr.update(value = instruction_pages[instruct_idx], visible=True),
                    instruction_btn_c: gr.update(visible=True),
                    topic_selections: gr.update(visible=False)
                } # not on next page yet
            else: 
                instruct_idx = 0
                return {
                experience_rating_html: gr.update(visible=True), 
                    experience_page_btn_c: gr.update(visible=True),
                    maths_bkgrd_experience: gr.update(visible=True), 
                    ai_interact_experience: gr.update(visible=True),
                    instruction_html: gr.update(visible=False),
                    instruction_btn_c: gr.update(visible=False),
                    topic_selections: gr.update(visible=True)
                } # shift page
            
        instruction_btn_c.click(
            update_instruction,
            [],
            [experience_rating_html, experience_page_btn_c, maths_bkgrd_experience, ai_interact_experience, instruction_html, instruction_btn_c, topic_selections]   
        )

    next_button.render()

    # Last page
    finish_page = gr.HTML("Thank you for participating in our study!", visible=False)

    def click():
        global problem_set_index

        # save out preferences for the current problem
        json.dump(
                {"prefence_data": []}, # convert b/c of weird numpy saving
                 open(os.path.join(unique_saving_path, unique_key, f"final_preferences_{problem_set_index}.json"), "w")
            )

        problem_set_index += 1

        # If this is the last batch of problems
        if problem_set_index >= len(poss_problems):
            return [gr.update(visible=True), gr.update(visible=False)] + [gr.update(visible=False) for _ in range(num_problems_show)]
        
        print("problems: ", poss_problems, poss_problems[problem_set_index])
        updated_boxes = [
            gr.update(visible=True) if poss_problems[problem_set_index]==i else gr.update(visible=False) for i in range(num_problems_show)
        ]

        if problem_set_index == len(poss_problems) - 1: 
            value = "Finish evaluating!"
        else:
            value = "Go to the next batch of problems"
        return [gr.update(visible=False), gr.update(visible=False, value=value)] + updated_boxes
    next_button.click(click, inputs=[], outputs=[finish_page, next_button] + boxes)

demo.queue()
demo.launch(share=True)

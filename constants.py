num_problems_show = 10 
num_models_show = 3
num_interactions = 20 

# each array is a new page
# elmts in an array should be new lines
# plaintxt_instructions = [
#     ["Welcome to our study!", "In this task, you will be interacting with AI systems to explore how well AI systems can assist in solving mathematical problems.", 
#      "Your responses will inform AI, mathematics, and potentially human-computer interaction research.",
#      "By participating in this study, you consent to having your responses stored and used for publication.",
#      "Your email and other identifying information (beyond level of mathematical expertise) will not be stored.", 
#      "Please only continue if you are comfortable with the above."],
#     ["In this study, you will be <strong>posed with a mathematical problem</strong> (e.g., a theorem) and asked to <strong>evaluate how good different AI systems are at <i>helping to solve</i> that problem.</strong>",
#      "For each problem, you will interact with <strong>" + str(num_models_show) + "</strong> different models.", 
#      "You will interact with each model for each problem."], 
#     # ["During the evaluation of model on a given problem, you will first see the unassisted generation of the model (i.e., the generation before any interaction).",
#     #  "You will be asked to rate the quality of this generation.",
#     #  "If the model perfectly solved the problem, indicate this in the rating. You will then move on to evaluating the next model."],
#      ["During the evaluation of model on a given problem, you will next get to <strong>interact</strong> with the model through a chat interface", 
#       "You have at most " + str(num_interactions) + " to play with the model and explore its ability to <i>help you solve the problem</i>. You do not need to use all interactions.",
#       "After these interactions, you will then rate the quality of each generated step.",
#       "Specifically: how <stong>helpful</strong> you found the response for helping you solve the problem, and how <strong>mathematically correct</strong> the response was."],
#       ["After rating the generations from each model for a given task, you will rate your <strong>preference</strong> over which model you would like as a <strong>mathematical assistant</strong>."],
#     ["Keep in mind that the order that each of the " + str(num_models_show) + " are presented in are shuffled for each new problem."],
#     ["You may evaluate a maximum of " + str(num_problems_show) + " problems for each of the three models. You can choose which subtopic of mathematics (e.g., algebra, probability theory) you would like these problems to come from.", 
#      "If you would like to stop evaluating early, you may end the study when you wish. Your data is saved as you go, and any evaluations are very much appreciated!",
#     ],
#     # ["If you do not understand the question, you may skip the problem. Otherwise, please try to solve it with the help of the AI.",
#     ["If you already know how to solve the problem, please imagine what kind of behavior you would like had you not been able to solve the problem."],
#      ["Now you are ready to begin!", 
#  "Remember: the order of the models will be shuffled for each set of three problems.", 
#  "Thank you for participating!"
#      ]
# ]

plaintxt_instructions = [
    ["Welcome to our study!", "In this task, you will be interacting with AI systems to explore how well AI systems can assist in solving mathematical problems.", 
     "Your responses will inform AI, mathematics, and potentially human-computer interaction research.",
     "By participating in this study, you consent to having your responses stored and used for publication.",
     "Your email and other identifying information (beyond level of mathematical expertise) will not be stored.", 
     "Please only continue if you are comfortable with the above."],
    ["In this study, you will be <strong>posed with mathematical problems</strong> (e.g., theorems) and asked to <strong>evaluate how good different AI systems are at <i>helping to solve</i> that problem.</strong>",    
    "You may evaluate a maximum of nine problems (three sets of three problems over the three models) You can choose which subtopic of mathematics (e.g., algebra, probability theory) you would like these problems to come from.", 
    "Note: if you already know how to solve the problem, pretend that you are an undergraduate mathematics student who does not immediately know how to solve the problem. What kind of assistance may be helpful? Are these AIs good assistants?"]]
    
    
first_rating_instructions = [

"You have at most " + str(num_interactions) + " interactions to play with the model and explore its ability to <i>help you solve the problem</i>. You do not need to use all interactions.",
 "After the interactions, you will rate <strong>for each step</strong>: 1) how <stong>helpful</strong> you found the response for helping you solve the problem, or if you already know how to solve the problem, imagine that you are an <strong>undergraduate student who does not immediately know how to solve the problem</strong>; and 2) how <strong>mathematically correct</strong> the response was.",
 "You can type in Markdown or LaTeX."

]
    
#     "During the evaluation of a model on a given problem, you will next get to <strong>interact</strong> with the model through a chat interface", 
#       "You have at most " + str(num_interactions) + " interactions to play with the model and explore its ability to <i>help you solve the problem</i>. You do not need to use all interactions.",
#       "After these interactions, you will then rate the quality of each generated step.",
#       "Specifically: how <stong>helpful</strong> you found the response for helping you solve the problem, or if you already know how to solve the problem, imagine that you are an <strong>undergraduate student who does not immediately know how to solve the problem</strong>; and how <strong>mathematically correct</strong> the response was.",
#     "After rating the generations from three different models on different problems, you will rate your <strong>preference</strong> over which model you would like as a <strong>mathematical assistant</strong>.", 
#     "You will then repeat this for another set of problems.", "Keep in mind that the order that each of the " + str(num_models_show) + " are presented in are shuffled for each new problem.", 
#     "You may evaluate a maximum of nine problems (three sets of three problems over the three models) You can choose which subtopic of mathematics (e.g., algebra, probability theory) you would like these problems to come from.", 
#      "If you would like to stop evaluating early, you may end the study when you wish. Your data is saved as you go, and any evaluations are very much appreciated!",
#     "<i>If you already know how to solve the problem, pretend that you are an undergraduate mathematics student who does not immediately know how to solve the problem. What kind of assistance may be helpful? Are these AIs good assistants?</i>"],
# #      ["Now you are ready to begin!", "Remember: the order of the models will be shuffled for each set of three problems.", 
# #  "Thank you for participating!"
# #      ]
# ]
# plaintxt_instructions = [
#     ["Welcome to our study!", "In this task, you will be interacting with AI systems to explore how well AI systems can assist in solving mathematical problems.", 
#      "Your responses will inform AI, mathematics, and potentially human-computer interaction research.",
#      "By participating in this study, you consent to having your responses stored and used for publication.",
#      "Your email and other identifying information (beyond level of mathematical expertise) will not be stored.", 
#      "Please only continue if you are comfortable with the above."],
#     ["In this study, you will be <strong>posed with mathematical problems</strong> (e.g., theorems) and asked to <strong>evaluate how good different AI systems are at <i>helping to solve</i> that problem.</strong>",    
#     "During the evaluation of a model on a given problem, you will next get to <strong>interact</strong> with the model through a chat interface", 
#       "You have at most " + str(num_interactions) + " interactions to play with the model and explore its ability to <i>help you solve the problem</i>. You do not need to use all interactions.",
#       "After these interactions, you will then rate the quality of each generated step.",
#       "Specifically: how <stong>helpful</strong> you found the response for helping you solve the problem, or if you already know how to solve the problem, imagine that you are an <strong>undergraduate student who does not immediately know how to solve the problem</strong>; and how <strong>mathematically correct</strong> the response was.",
#     "After rating the generations from three different models on different problems, you will rate your <strong>preference</strong> over which model you would like as a <strong>mathematical assistant</strong>.", 
#     "You will then repeat this for another set of problems.", "Keep in mind that the order that each of the " + str(num_models_show) + " are presented in are shuffled for each new problem.", 
#     "You may evaluate a maximum of nine problems (three sets of three problems over the three models) You can choose which subtopic of mathematics (e.g., algebra, probability theory) you would like these problems to come from.", 
#      "If you would like to stop evaluating early, you may end the study when you wish. Your data is saved as you go, and any evaluations are very much appreciated!",
#     "<i>If you already know how to solve the problem, pretend that you are an undergraduate mathematics student who does not immediately know how to solve the problem. What kind of assistance may be helpful? Are these AIs good assistants?</i>"],
# #      ["Now you are ready to begin!", "Remember: the order of the models will be shuffled for each set of three problems.", 
# #  "Thank you for participating!"
# #      ]
# ]


# formatted with center align for each 
# instruction_pages = ["".join(['<p style="text-align:center">' + x + "</p>" for x in instruction_page]) for instruction_page in plaintxt_instructions]
instruction_pages = ["".join(['<p style="text-align:left">' + x + "</p>" for x in instruction_page]) for instruction_page in plaintxt_instructions]
first_rating_instruct_txt = "".join(['<p style="text-align:left">' + x + "</p>" for x in first_rating_instructions]) 

wellcome_html_content = ""
# wellcome_html_content = '<p style="text-align:center"> You will now evaluate a model\'s </p>' + \
#     '<p style="text-align:center"> Please click <strong>\"Next\"</strong> to start the interactions.</p>' + \
#     '<p style="text-align:center"> Remember: the order of the models will be shuffled for each set of three problems. </p>' + \
#     '<p style="text-align:center"> Thank you for participating! </p>'

# wellcome_html_content = '<p style="text-align:center"> Now you are ready to begin! </p>' + \
#     '<p style="text-align:center"> Please click <strong>\"Next\"</strong> to start the interactions.</p>' + \
#     '<p style="text-align:center"> Remember: the order of the models will be shuffled for each set of three problems. </p>' + \
#     '<p style="text-align:center"> Thank you for participating! </p>'

experience_options = ["Current undergraduate studying mathematics", 
                      "Undegraduate degree in mathematics",
                      "Masters degree in mathematics",
                      "PhD in mathematics",
                      "Professor in mathematics",
                      "Never studied for a math degree / not enrolled in math degree"]


ai_experience_options = ["Never",
                         "A few times total",
                         "A couple of times a month",
                         "Weekly",
                         "Daily"]

# useful_prompt_txt = "How useful is the generation to help solve the task (e.g., as a hint)?"
# useful_prompt_txt = "How helpful is the generation toward helping you, or an appropriately experienced student, solve the problem?"
useful_prompt_txt = "How helpful would this AI generated response be towards helping someone solve this problem? If you already know how to solve the problem, evaluate this as if you were an undergraduate mathematics student encountering this problem for the first time."

correctness_prompt_txt = "How correct (i.e., mathematically sound) is the generation?"

# usefulness_options = [
#     "Definitely useless",
#     "Largely useless",
#     "Somewhat useless",
#     "May be useful",
#     "Somewhat useful",
#     "Largely useful",
#     "Definitely useful"
# ]

usefulness_options = [
    "(0) Actively harmful",
    "(1) Very harmful",
    "(2) Somewhat harmful",
    "(3) Unlikely to help, but unlikely to hurt",
    "(4) Somewhat helpful",
    "(5) Very helpful",
    "(6) Definitely helpful"
]

# correctness_options = [
#     "(0) Completely nonsensical",
#     "(1) Multiple critical maths errors", 
#     "(2) At least one critical maths error, or many small errors", 
#     "(3) Decent error(s), but mostly correct otherwise", 
#     "(4) Small maths error, but largely correct", 
#     # "Possibly a small error, but otherwise corret",
#     "Completely correct"
# ]

correctness_options = [
    "(0) N/A - this response does not contain any mathematical information",
    "(1) Completely incorrect or nonsensical", 
    "(2) Multiple critical maths errors",
    "(3) At least one critical math error or multiple small errors",
    "(4) One or more minor errors, but otherwise mostly correct",
    "(5) One or two minor errors, but almost entirely correct",
    "(6) Completely correct"
]


solo_solve_options = [
    "(0) Definitely could not solve on my own",
    "(1) Very unlikely to be able to solve on my own",
    "(2) Unlikely to be able to solve on my own", 
    "(3) May be able to solve on my own",
    "(4) Likely be able to solve on my own",
    "(5) Very likely to be able to solve on my own", 
    "(6) Definitely can solve on my own"
    ]

error_options = [
    "Syntax error",
    "Improper algebraic manipulation",
    "Wrong inequality direction"
]

yes_no_options = [
    "Yes",
    "No"
]

model_options = [
    "chatgpt",
    # "codegpt",
    # "textgpt",
    "instructgpt",
    "chatgpt4"
]


MAX_CONVERSATION_LENGTH = 20
MAX_TOKENS_PER_GENERATION = 512

SAMPLING_TEMPERATURE = 0.
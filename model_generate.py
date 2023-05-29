from constants import model_options, MAX_CONVERSATION_LENGTH, MAX_TOKENS_PER_GENERATION, SAMPLING_TEMPERATURE

import gradio as gr
import openai 

oai_key = "" # ADD YOUR KEY
openai.api_key = oai_key


def generate(model, prompt):
    assert model in model_options
    if model == "codegpt" or model == "textgpt" or model == "instructgpt":
        oai_model_name = {
            "codegpt": "code-davinci-002",
            "textgpt": "text-davinci-003",
            "instructgpt": "text-davinci-003"
        }
        completion = openai.Completion.create(
            model=oai_model_name[model],
            prompt=prompt,
            max_tokens=256,
            temperature=0,
            stop=["Question:"]
        )
        return completion.choices[0].text
    elif model == "chatgpt" or model == "chatgpt4":
        oai_model_name = {
            "chatgpt": "gpt-3.5-turbo",
            "chatgpt4": "gpt-4"
        }
        message_string = prompt.replace("Question:", "<delim>user:")
        message_string = message_string.replace("Answer:", "<delim>assistant:")
        messages = message_string.split("<delim>")
        messages = [m.strip() for m in messages]
        messages = [m for m in messages if m]
        conversation = []
        for message in messages:
            if message.startswith("user:"):
                conversation.append({"role": "user", "content": message[5:]})
            elif message.startswith("assistant:"):
                conversation.append({"role": "assistant", "content": message[10:]})
            else:
                raise AssertionError(message)
        conversation = [{"role": "system", "content": "You are an assistant to a professional mathematician."}, conversation[-2]]
        sentence = openai.ChatCompletion.create(
            model=oai_model_name[model],
            messages=conversation,
            max_tokens=256
        )
        return sentence.choices[0].message.content
    else:
        raise NotImplementedError

def generate_with_chatbot_divisors(model, prompt):
    return openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=256,
        temperature=0,
        stop=["User:", "AI:"]
    )["choices"][0]["text"]


def legacy_chatbot_generate(user_input, history=[]):
    history.append(f"User: {user_input.strip()}")
    prompt = "\n".join(history) + f"\nAI:"
    response = generate_with_chatbot_divisors(None, prompt)
    history.append(f"AI: {response.strip()}")
    conversations = [(history[i], history[i+1]) for i in range(0, len(history)-1, 2)]

    # Whether the textbox and the submit button should be hidden
    if len(history) >= 2*MAX_CONVERSATION_LENGTH:
        return conversations, history, gr.update(visible=False), gr.update(visible=False)
    else:
        return conversations, history, gr.update(visible=True), gr.update(visible=True)


########################################
# The above should not be used anymore #
########################################
def query_a_chat_completion(model, messages):
    assert model in ["gpt-3.5-turbo", "gpt-4"]
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=MAX_TOKENS_PER_GENERATION,
        temperature=SAMPLING_TEMPERATURE
    )
    return completion.choices[0].message.content

def pretend_a_chat_completion(model, messages):
    assert model == "text-davinci-003"
    # Create an instruction prompt
    prompt = "Help a professional mathematician solve a problem:\n"
    for message in messages:
        if message["role"] == "user":
            prompt += f"User: {message['content']}\n"
        elif message["role"] == "assistant":
            prompt += f"AI: {message['content']}\n"
        else:
            pass
    prompt += "AI:"
    # print(prompt)
    completion = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=MAX_TOKENS_PER_GENERATION,
        temperature=SAMPLING_TEMPERATURE
    )
    return completion["choices"][0]["text"]


def chatbot_generate(user_newest_input, history, model):
    """
    Generate the next response from the chatbot
    :param user_newest_input: The newest input from the user
    :param history: The history of the conversation
        list[str], where each element starts with "User:" or "AI:"
    :return: The chatbot state, the history, the text, the submit button
    """
    # convert to openai model format
    actual_model = {
        "chatgpt": "gpt-3.5-turbo",
        "chatgpt4": "gpt-4",
        "instructgpt": "text-davinci-003"
    }[model]

    # Update the history with newest user input
    history.append(f"User: {user_newest_input.strip()}")

    # construct chat messages
    chat_messages = [{"role": "system", "content": "You are a helpful assistant to a professional mathematician."}]
    for hist in history:
        if hist.startswith("User:"):
            chat_messages.append(
                {
                    "role": "user",
                    "content": hist[5:].strip()
                }
            )
        elif hist.startswith("AI:"):
            chat_messages.append(
                {
                    "role": "assistant",
                    "content": hist[3:].strip()
                }
            )
        else:
            raise NotImplementedError
    
    # Get the generation from OpenAI
    if actual_model in ["gpt-3.5-turbo", "gpt-4"]:
        ai_newest_output = query_a_chat_completion(actual_model, chat_messages)
    elif actual_model == "text-davinci-003":
        ai_newest_output = pretend_a_chat_completion(actual_model, chat_messages)
    else:
        raise NotImplementedError
    
    # Update the history with newest AI output
    history.append(f"AI: {ai_newest_output.strip()}")
    conversations = [(history[i], history[i+1]) for i in range(0, len(history)-1, 2)]

    # Whether the textbox and the submit button should be hidden
    if len(history) >= 2*MAX_CONVERSATION_LENGTH:
        return conversations, history, gr.update(visible=False), gr.update(visible=False)
    else:
        return conversations, history, gr.update(visible=True), gr.update(visible=True)

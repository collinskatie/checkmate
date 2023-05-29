import os


ones_digit_to_ones_digit_of_examples = {}
for i in range(10):
    ones_digit_to_ones_digit_of_examples[i] = [1]
ones_digit_to_ones_digit_of_examples[1] = [2]
# ones_digit_to_ones_digit_of_examples[2] = [1]
# ones_digit_to_ones_digit_of_examples[3] = [1]


def construct_one_example(question, answer):
    return f"Question: {question}\nAnswer: {answer}".strip()


def get_prompt_examples(prompt_dir):
    """
    We expect the examples in the prompt directory to be named p{x}_{question|answer}.md
    Output of this function:
        {
            {problem_id}: {
                "question": {question},
                "answer": {answer}
            }
        }
    """
    problem_index_to_info = {}
    for file in os.listdir(prompt_dir):
        if file.endswith(".md"):
            index, question_or_answer = file.rstrip(".md").split("_")
            index = int(index.lstrip("p"))
            assert question_or_answer in ["question", "answer"]

            file_path = os.path.join(prompt_dir, file)
            with open(file_path, "r") as f:
                text = f.read().strip()


            if index not in problem_index_to_info:
                problem_index_to_info[index] = {
                    question_or_answer: text
                }
            else:
                problem_index_to_info[index][question_or_answer] = text

    assert len(problem_index_to_info) == 6 * 4
    for value in problem_index_to_info.values():
        assert len(value) == 2
    return problem_index_to_info


def construct_prompt(problem_id, problem_text, prompt_examples):
    """
    For each of the six domains, we prepare 4 examples in the format of (question, answer)
    These correspond to the first 4 problems of each domain, i.e., p1-4, p11-14, p21-24, p31-34, p41-44, p51-54
    To construct the prompts, we use 3 examples that are different from the problem at hand
    E.g., for p1, we use p2, p3, and p4 as the prompts
        for p2, we use p1, p3, and p4 as the prompts
        for p3, we use p1, p2, and p4 as the prompts
        for p4-10, we use p1, p2, and p3 as the prompts
    """
    assert 1 <= problem_id <= 60
    tens_digit, ones_digit = divmod(problem_id, 10)
    ones_digit_of_examples = ones_digit_to_ones_digit_of_examples[ones_digit]
    indices_of_examples = [10 * tens_digit + i for i in ones_digit_of_examples]

    total_examples = "\n".join(
        construct_one_example(prompt_examples[index]["question"].strip(), prompt_examples[index]["answer"].strip()) for index in indices_of_examples
    ).strip()
    entire_prompt = total_examples + f"\nQuestion: {problem_text.strip()}\nAnswer:"
    return entire_prompt

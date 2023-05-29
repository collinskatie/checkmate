import os

categories = {}
for i, category in enumerate(
    [
        "Algebra",
        "Group theory",
        "Number theory",
        "Probability theory",
        "Topology",
        "Linear algebra",
    ]
):
    for j in range(10):
        categories[i * 10 + j + 1] = category


def load_problem(problem_dir, use_html=False):
    """Load a problem from the problem directory."""
    if use_html:
        problem_file_name = problem_dir.split("/")[-1].rstrip(".html")
    else:
        problem_file_name = problem_dir.split("/")[-1].rstrip(".md")
    problem_file_name_split = problem_file_name.split("_")
    print("problem file name: ", problem_file_name_split)
    problem_id = int(problem_file_name_split[0][1:]) # remove the starting "p"
    problem_name = "_".join(problem_file_name_split[1:])
    problem_category = categories[problem_id]
    with open(problem_dir, "r") as f:
        problem_text = f.read()
        return {
            "id": problem_id,
            "name": problem_name,
            "text": problem_text,
            "category": problem_category,
        }


def load_problems(problems_path, use_html=False):
    """Load all problems from the problems directory."""
    problems = []
    for problem_dir in sorted(os.listdir(problems_path)):
        problem_id = int(problem_dir.split("_")[0][1:])
        problem_dir = os.path.join(problems_path, problem_dir)
        assert os.path.isfile(problem_dir)
        problem = load_problem(problem_dir, use_html=use_html)
        problems.append((problem_id, problem))

    problems = sorted(problems, key=lambda x: x[0])
    problems = [problem for _, problem in problems]
    return problems

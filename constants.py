MAX_CONVERSATION_LENGTH = 20
MAX_TOKENS_PER_GENERATION = 512
SAMPLING_TEMPERATURE = 0.


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

"You have at most " + str(MAX_CONVERSATION_LENGTH) + " interactions to play with the model and explore its ability to <i>help you solve the problem</i>. You do not need to use all interactions.",
 "After the interactions, you will rate <strong>for each step</strong>: 1) how <stong>helpful</strong> you found the response for helping you solve the problem, or if you already know how to solve the problem, imagine that you are an <strong>undergraduate student who does not immediately know how to solve the problem</strong>; and 2) how <strong>mathematically correct</strong> the response was.",
 "You can type in Markdown or LaTeX."

]

instruction_pages = ["".join(['<p style="text-align:left">' + x + "</p>" for x in instruction_page]) for instruction_page in plaintxt_instructions]
first_rating_instruct_txt = "".join(['<p style="text-align:left">' + x + "</p>" for x in first_rating_instructions]) 

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


useful_prompt_txt = "How helpful would this AI generated response be towards helping someone solve this problem? If you already know how to solve the problem, evaluate this as if you were an undergraduate mathematics student encountering this problem for the first time."

correctness_prompt_txt = "How correct (i.e., mathematically sound) is the generation?"

usefulness_options = [
    "(0) Actively harmful",
    "(1) Very harmful",
    "(2) Somewhat harmful",
    "(3) Unlikely to help, but unlikely to hurt",
    "(4) Somewhat helpful",
    "(5) Very helpful",
    "(6) Definitely helpful"
]

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

model_options = [
    "chatgpt",
    "instructgpt",
    "chatgpt4"
]


import os
import re

definition_chars = "\[\[Definition:"
starting_chars = "\[\["
ending_chars = "\]\]"

if __name__ == "__main__":
    path_to_clean = "data/prompts"
    for filename in os.listdir(path_to_clean):
        if filename.endswith(".md"):
            with open(os.path.join(path_to_clean, filename), "r") as f:
                text = f.read()
                indices_to_del = []
                for m in re.finditer(definition_chars, text):
                    start_m = m.start()
                    first_divisor = text[start_m:].find("|")
                    first_end = text[start_m:].find("]]")

                    indices_to_del.extend(
                        list(range(start_m, start_m + first_divisor + 1))
                    )
                    indices_to_del.extend(
                        [start_m + first_end, start_m + first_end + 1]
                    )
                altered_text = "".join(
                    [c for i, c in enumerate(text) if i not in indices_to_del]
                )
                # print(text)
                # print(altered_text)
                # print("*" * 100)

                for s in [m.start() for m in re.finditer(starting_chars, text)]:
                    indices_to_del.extend([s, s + 1])

                for s in [m.start() for m in re.finditer(ending_chars, text)]:
                    indices_to_del.extend([s, s + 1])

            with open(os.path.join(path_to_clean, filename), "w") as f:
                f.write(altered_text)

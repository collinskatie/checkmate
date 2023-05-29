import os
from bs4 import BeautifulSoup


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="input markdown directory")
    parser.add_argument("output_dir", help="output html directory")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename.replace(".md", ".html"))
            print("Rendering {} to {}".format(input_path, output_path))
            os.system("pandoc -f markdown -t html --webtex='https://latex.codecogs.com/svg.latex?' {} -o {}".format(input_path, output_path))

    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)

        file_content = open(file_path, "r").read()
        file_content = file_content.replace(
            '<img style="', '<img style="display:inline-block;'
        )
        soup = BeautifulSoup(file_content, "html.parser")
        for img in soup.find_all("img"):
            img["alt"] = f'${img["alt"]}$'
        file_content = str(soup)
        with open(file_path, "w") as f:
            f.write(file_content)

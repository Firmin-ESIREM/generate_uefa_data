from os.path import join


def load_csv(filename: str) -> list:
    with open(join("input_data", filename + ".csv"), 'r') as f:
        content = f.read()
    content = content.split("\n")
    header = content[0].split(';')
    content.pop(0)
    content_formatted = []
    for line in content:
        if line != '':
            split_line = line.split(';')
            line_content = {}
            for i, field in enumerate(header):
                line_content[field] = split_line[i]
            content_formatted.append(line_content)
    return content_formatted

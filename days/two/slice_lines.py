def slice_lines(path: str):
    file = open(path, 'r')
    lines = file.readlines()
    lines_formatted = []

    # remove \n in line
    for line in lines:
        formatted_line = line.replace('\n', '')
        lines_formatted.append(formatted_line)

    return lines_formatted

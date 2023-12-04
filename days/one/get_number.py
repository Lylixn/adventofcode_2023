def get_number(line: str):
    start_i = 0
    end_i = len(line)

    numbers = 0

    for i in range(start_i, end_i):
        if line[i].isdigit():
            print('----> ', int(line[i]))
            numbers += int(line[i]) * 10
            break
    for i in reversed(range(start_i, end_i)):
        if line[i].isdigit():
            print('----> ', int(line[i]))
            numbers += int(line[i])
            break
    return numbers

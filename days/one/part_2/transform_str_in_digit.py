def number_to_str(str_digit: str):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if str_digit in numbers:
        return numbers.index(str_digit) + 1

    return 'zero'


def transform_str_in_digit(line: str):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    first = {
        'index': len(line) + 1,
        'number': ''
    }
    last = {
        'index': -1,
        'number': ''
    }

    for number in numbers:
        i = line.find(number)
        if i != -1:
            if i < first['index']:
                first = {
                    'index': i,
                    'number': number
                }
    for number in numbers:
        i = line.find(number)
        if i != -1:
            if i > last['index']:
                last = {
                    'index': i,
                    'number': number
                }
    if first['number']:
        num = first['number']
        line = line.replace(num, str(number_to_str(num)))
    if last['number']:
        num = last['number']
        line = line.replace(num, str(number_to_str(num)))
    return line

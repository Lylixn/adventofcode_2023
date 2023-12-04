from days.one.get_number import get_number
from days.one.part_2.transform_str_in_digit import transform_str_in_digit
from days.one.slice_lines import slice_lines


def day1_part2(launch_type: str):
    path = './assets/day1_part2.txt' if launch_type == 'test' else './assets/day1.txt'
    lines = slice_lines(path)
    total = 0
    for line in lines:
        line = transform_str_in_digit(line)
        print(line)
        num = get_number(line)
        print("total line : ", num, '\n')
        total += num

    print('total : ', total)

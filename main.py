import sys

from days.one.part_1.main import day1_part1
from days.one.part_2.main import day1_part2


def main():
    if len(sys.argv) > 1:
        day = sys.argv[1]
        launch_type = 'normal'
        if len(sys.argv) >= 3:
            launch_type = 'test' if sys.argv[2] == 'test' else 'normal'

        if day == '1.1':
            day1_part1(launch_type)
        if day == '1.2':
            day1_part2(launch_type)
        return


if __name__ == '__main__':
    main()

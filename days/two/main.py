from days.two.game import Game
from days.two.slice_game import slice_game
from days.two.slice_lines import slice_lines
from days.two.slice_sort import slice_sort
from days.two.sort import Sort


def day2(launch_type):
    path = './assets/day2_test1.txt' if launch_type == 'test' else './assets/day2.txt'
    lines = slice_lines(path)

    total = 0

    for line in lines:
        sort: list[Sort] = slice_sort(line[8:])
        game_id: int = slice_game(line[:8])
        game = Game(
            game_id=game_id,
            sort=sort
        )

        if game.is_valid():
            total += game.game_id

    print(total)

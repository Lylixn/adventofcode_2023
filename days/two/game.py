from days.two.sort import Sort


class Game:
    game_id: int
    sort: list[Sort]
    expected_red: int
    expected_green: int
    expected_blue: int

    def __init__(self, game_id: int, sort: list[Sort]):
        self.game_id = game_id
        self.sort = sort
        self.expected_red = 12
        self.expected_green = 13
        self.expected_blue = 14

    def is_valid(self):
        max_green = 0
        max_red = 0
        max_blue = 0

        for sort in self.sort:
            if sort.get_red() > max_red:
                max_red = sort.red
            if sort.get_green() > max_green:
                max_green = sort.green
            if sort.get_blue() > max_blue:
                max_blue = sort.blue

        return max_red <= self.expected_red and max_green <= self.expected_green and max_blue <= self.expected_blue


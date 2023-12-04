color_list = ['red', 'green', 'blue']


class Sort:
    green: int = 0
    blue: int = 0
    red: int = 0

    def __init__(self, sort_string: str):
        colors = sort_string.split(',')
        for color in colors:
            color_number = ''
            for i in range(0, len(color)):
                if color[i].isdigit():
                    color_number += color[i]
            color_number = int(color_number)
            for color_set in color_list:
                if color_set in color:
                    if color_set == 'red':
                        self.red = color_number
                    elif color_set == 'green':
                        self.green = color_number
                    elif color_set == 'blue':
                        self.blue = color_number
                    break
        print('--> red: ', self.red, ' green: ', self.green, ' blue: ', self.blue)

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

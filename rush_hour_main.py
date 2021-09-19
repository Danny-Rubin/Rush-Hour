import itertools  #for generating car id
from example_board_22 import *
new_id = itertools.count()

class Car:
    def __init__(self, is_vertical, color, length):
        self.is_vertical = is_vertical
        self.color = color
        self.is_red = self.color == "red"
        self.length = length
        self.id = hex(new_id.__next__())[2:]

    # a func that codes the car color to a short str
	@staticmethod
    def color_code(self):
        if " " not in self.color:
            return self.color[:2]
        else:
        	color_words = self.color.split(" ")  # in case the name contains few words
			return color_words[0][0] + color_words[1][0]
        # what about another way to prevent identical color codes like a dict????

    def __repr__(self):
        return self.color    # in order to print car objects


class Board:
    def __init__(self, board_dict, n, prev_board=None, prev_step=None):
        self.board_dict = board_dict
        self.n = n
        self.next_list = [] # TDL: write a func that finds this list
        self.prev_board = prev_board
        self.prev_step = prev_step
        self.id = ""    # TDL: create a function that converts board to id"

    def get_path(self):
        path = ""
        if self.prev_board == None:
            path += "starting board \n | \n V"
        else:
            path += self.prev_board.get_path()
        path += self.prev_step + "\n | \n V "
        return path


def main():
    print(board_dict_22)
    start_board = Board(board_dict_22, 6)
    print(start_board.prev_board)


if __name__ == '__main__':
    main()

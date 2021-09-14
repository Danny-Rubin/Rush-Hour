import itertools  #for generating car id
import operator

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
    def color_code(self):
        color_words = self.color.split(" ")  # in case the name contains few words
        col_code = ""
        for word in color_words:
            col_code += word[:2]
        return col_code
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
    
    @staticmethod
    def is_solved(self, n):
        pass
    
    @staticmethod
    def next_boards(self, board_set, n)
        vacancy_mat = self.vacancy_mat()
        res = []
        for item in self.board_dict.items():
            car,  pos_i, pos_j =  item[0], item[1][0], item[1][1]
            step = (0,1) if car.is_vertical else (1,0)
            pos_i, pos_j = tuple(map(operator.sub((pos_i,pos_j), step)))
          
            while pos_i > 0 and pos_j > 0 and not vacancy_mat[pos_i][pos_j]:
                new_board_dict = self. board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, n, self, "move " + str(car) + " to: " + (pos_i, pos_j))
                res.append(new_board)
                pos_i, pos_j = tuple(map(operator.sub((pos_i,pos_j), step)))
            pos_i, pos_j = item[1][0], item[1][1]
            pos_i, pos_j += step*(car.length-1)
            
            while pos_i < n and pos_j < n and not vacancy_mat[pos_i][pos_j]:
                new_board_dict = self. board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, n, self, "move " + str(car) + " to: " + (pos_i, pos_j))
                res.append(new_board)
                pos_i, pos_j += step
            
            
                

def main():
    print(board_dict_22)
    start_board = Board(board_dict_22, 6)
    print(start_board.prev_board)


if __name__ == '__main__':
    main()

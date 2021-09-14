import itertools  #for generating car id
import operator

from example_board_22 import *
new_id = itertools.count()

def forward(tup, car_direction, steps):
    res = tup
    if car_direction == "down":
        res = (tup[0]+steps, tup[1])
    else:
        res = (tup[0], tup[1]+steps)
    return res

def backward(tup, car_direction, steps):
    res = tup
    if car_direction == "down":
        res = (tup[0]-steps, tup[1])
    else:
        res = (tup[0], tup[1]-steps)
    return res

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
            car_direction = "down" if car.is_vertical else "right"
            pos_i, pos_j = backward((pos_i, pos_j), car_direction, 1))
          
            while pos_i > 0 and pos_j > 0 and not vacancy_mat[pos_i][pos_j]:
                new_board_dict = self. board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, n, self, "move " + str(car) + " to: " + (pos_i, pos_j))
                if not new_board in board_set:
					res.append(new_board)
                pos_i, pos_j = backward((pos_i, pos_j), car_direction, 1))
                
            pos_i, pos_j = item[1][0], item[1][1]
           
            pos_i, pos_j = forward((pos_i, pos_j), car_direction, 1))
			front_pos_i, front_pos_j =forward((pos_i, pos_j), car_direction, (car.length-1))
            while front_pos_i < n and front_pos_j < n and not vacancy_mat[front_pos_i][front_pos_j]:
                new_board_dict = self. board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, n, self, "move " + str(car) + " to: " + (pos_i, pos_j))
				if not new_board.id in board_set:
					res.append(new_board)
                pos_i, pos_j = forward((pos_i, pos_j), car_direction, 1))
	return res
            
          
                

def main():
    print(board_dict_22)
    start_board = Board(board_dict_22, 6)
    print(start_board.prev_board)


if __name__ == '__main__':
    main()

import itertools  #for generating car id
from example_board_22 import *
new_id = itertools.count()

RED_CAR_LEN = 2

def is_solved(board, n):
    car_front_pos = forward(board.red_car_pos, "right", RED_CAR_LEN-1)
    vac_mat = board.vacancy_mat()
    while car_front_pos[1] < n - 1:
        if vac_mat[car_front_pos[0]][car_front_pos[1] + 1] == True:
            return False
        car_front_pos = forward(car_front_pos, "right", 1)
    return True

def solve(start, n=6):
    solved = False
    curr_level = [start]
    board_set = {start.id}
    while not solved:
        next_level = []
        for board in curr_level:
            if is_solved(board,n):
                print(board.get_path(), "\n WIN")
                solved = True
                break
            board.next_list = board.next_boards(board_set, n)
            next_level.extend(board.next_list)
            board_set.update([x.id for x in board.next_list])
        curr_level = next_level

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


# noinspection PyDecorator
class Car:
    def __init__(self, is_vertical, color, length):
        self.is_vertical = is_vertical
        self.color = color
        self.is_red = self.color == "red"
        self.length = length
        self.id = hex(new_id.__next__())[2:]

    # a func that codes the car color to a short str

    #@staticmethod
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
        for car in self.board_dict.keys():
            if car.color == "red":
                self.red_car_pos = self.board_dict[car]
                break
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
    def next_boards(self, board_set, n):
        vacancy_mat = self.vacancy_mat()
        res = []
        for item in self.board_dict.items():
            car,  pos_i, pos_j =  item[0], item[1][0], item[1][1]
            car_direction = "down" if car.is_vertical else "right"
            pos_i, pos_j = backward((pos_i, pos_j), car_direction, 1)
          
            while pos_i > 0 and pos_j > 0 and not vacancy_mat[pos_i][pos_j]:
                new_board_dict = self. board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, n, self, "move " + str(car) + " to: " + (pos_i, pos_j))
                if not new_board.get_id() in board_set:
                    res.append(new_board.get_id())
                    board_set.add(new_board.get_id())
                pos_i, pos_j = backward((pos_i, pos_j), car_direction, 1)
                
            pos_i, pos_j = item[1][0], item[1][1]
           
            pos_i, pos_j = forward((pos_i, pos_j), car_direction, 1)
            front_pos_i, front_pos_j =forward((pos_i, pos_j), car_direction, (car.length-1))
            while front_pos_i < n and front_pos_j < n and not vacancy_mat[front_pos_i][front_pos_j]:
                new_board_dict = self. board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, n, self, "move " + str(car) + " to: " + (pos_i, pos_j))
                if not new_board.get_id() in board_set:
                    res.append(new_board.get_id())
                    board_set.add(new_board.get_id())
                pos_i, pos_j = forward((pos_i, pos_j), car_direction, 1)
        return res

    def print_board(self):
        n = self.n
        board = self
        mat = [["xx" for i in range(n)] for j in range(n)]
        for car in board.board_dict.keys():
            code = car.color_code()
            for coordinate in car_coordinates(car, board.board_dict[car]):
                mat[coordinate[0]][coordinate[1]] = code

        print_matrix(mat)
        return


#mat = [["a1", "b2", "c3"], ["d1", "b2", "c3"], ["a1", "e2", "c3"]]

        
    def vacancy_mat(self):
        vac_mat = [[False for i in range(self.n)] for j in range(self.n)]
        for car in self.board_dict.keys():
            for i in range(car.length):
                vac_mat[board_dict[car][0] + i*car.is_vertical][board_dict[car][1] + i*(not car.is_vertical)] = True
        return vac_mat


def print_matrix(mat):
    n = len(mat)
    for row in mat:
        for item in row:
            print(item, end = " ")
        print()      
          

def car_coordinates(car, position):
    res = []
    for i in range(car.length):
        res.append((position[0] + i*car.is_vertical, position[1]+ i*(not car.is_vertical)))
    return res

def main():
#     print(board_dict_22)
    start_board = Board(board_dict_22, 6)
#     print(start_board.prev_board)
#     start_board.print_board()
    solve(start_board, 6)


if __name__ == '__main__':
    main()

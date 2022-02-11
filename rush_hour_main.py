import itertools  # for generating car id
import time
from color_text import *
import solve_game

new_id = itertools.count()
RED_CAR_LEN = 2

# this function returns a unique identifier of a board given a board-dict. returns string.
def get_id(my_dict):
    dict_id = sorted([str(x[0]) + ": " + str(x[1]) for x in my_dict.items()])
    return ", ".join(dict_id)



def forward(tup, car_direction, steps):
    """
    This function takes a car and moves it forward in the given amount of steps
    :param tup: tuple of indices (x,y) that represent the position of the leftmost or upper car in the matrix
    :param car_direction: direction in which we want to move the car (down or right)
    :param steps:
    :return: the position of the moved car
    """
    res = tup
    if car_direction == "down":
        res = (tup[0] + steps, tup[1])
    else:
        res = (tup[0], tup[1] + steps)
    return res


def backward(tup, car_direction, steps):
    # same like forward but moves backward
    res = tup
    if car_direction == "down":
        res = (tup[0] - steps, tup[1])
    else:
        res = (tup[0], tup[1] - steps)
    return res


class Car:
    def __init__(self, is_vertical, color, length):
        self.is_vertical = is_vertical    # boolean field- true or false
        self.color = color
        self.is_red = self.color == "red"
        self.length = length
        self.id = hex(new_id.__next__())[2:]

    def color_code(self):   # this method returns a two-char unique code of the car
        if " " not in self.color:
            return self.color[:2]
        else:
            color_words = self.color.split(" ")  # in case the name contains few words
            return color_words[0][0] + color_words[1][0]

    def __repr__(self):
        return self.color  # in order to print car objects


class Board:
    def __init__(self, board_dict, n, prev_board=None, prev_step=None):
        self.board_dict = board_dict     # dict of cars:[x,y] where the edge of the car is in entry [x,y]
        self.n = n
        self.next_list = []
        self.prev_board = prev_board    # A board object, points the previous board before making the previous step
        self.prev_step = prev_step      # A string to describe the last step done in the solving process
        for car in self.board_dict.keys():  # finding the postion of the red car:
            if car.color == "red":
                self.red_car_pos = self.board_dict[car]
                break
        self.id = ""

    def print_path(self):
        if self.prev_board is None:
            self.print_board()

        else:
            self.prev_board.print_path()
            print(self.prev_step)
            print()
            self.print_board()
        if self.next_list == []:
            print("WIN: The red car has a clear path \n")

    @staticmethod
    def is_solved(self):
        car_front_pos = forward(self.red_car_pos, "right", RED_CAR_LEN - 1)
        vac_mat = self.vacancy_mat()
        while car_front_pos[1] < self.n - 1:
            if vac_mat[car_front_pos[0]][car_front_pos[1] + 1]:
                return False
            car_front_pos = forward(car_front_pos, "right", 1)
        return True

    @staticmethod
    def next_boards(self, board_set):
        vacancy_mat = self.vacancy_mat()
        res = []
        for item in self.board_dict.items():
            car, pos_i, pos_j = item[0], item[1][0], item[1][1]
            car_direction = "down" if car.is_vertical else "right"
            pos_i, pos_j = backward((pos_i, pos_j), car_direction, 1)

            while pos_i >= 0 and pos_j >= 0 and not vacancy_mat[pos_i][pos_j]:
                new_board_dict = self.board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                my_id = get_id(new_board_dict)
                if not my_id in board_set:
                    new_board = Board(new_board_dict, self.n, self, "move " + str(car) + " to: " + str((pos_i, pos_j)))
                    res.append(new_board)
                    board_set.add(my_id)
                pos_i, pos_j = backward((pos_i, pos_j), car_direction, 1)

            pos_i, pos_j = item[1][0], item[1][1]

            pos_i, pos_j = forward((pos_i, pos_j), car_direction, 1)
            front_pos_i, front_pos_j = forward((pos_i, pos_j), car_direction, (car.length - 1))
            while front_pos_i < self.n and front_pos_j < self.n and not vacancy_mat[front_pos_i][front_pos_j]:
                new_board_dict = self.board_dict.copy()
                new_board_dict[car] = [pos_i, pos_j]
                new_board = Board(new_board_dict, self.n, self, "move " + str(car) + " to: " + str((pos_i, pos_j)))
                my_id = get_id(new_board_dict)
                if not my_id in board_set:
                    res.append(new_board)
                    board_set.add(my_id)
                pos_i, pos_j = forward((pos_i, pos_j), car_direction, 1)
                front_pos_i, front_pos_j = forward((front_pos_i, front_pos_j), car_direction, 1)
        return res

    def print_board(self):
        n = self.n
        board = self
        mat = [["xx" for i in range(n)] for j in range(n)]
        for car in board.board_dict.keys():
            code = car.color_code()
            for coordinate in car_coordinates(car, board.board_dict[car]):
                mat[coordinate[0]][coordinate[1]] = code

        for i in range(4 * n):
            print("#", end='')
        print()
        print_color_matrix(mat)
        for i in range(4 * n):
            print("#", end='')
        print()
        print()
        return

    def vacancy_mat(self):
        vac_mat = [[False for i in range(self.n)] for j in range(self.n)]
        for car in self.board_dict.keys():
            for i in range(car.length):
                vac_mat[self.board_dict[car][0] + i * car.is_vertical][
                    self.board_dict[car][1] + i * (not car.is_vertical)] = True
        return vac_mat


def print_matrix(mat):
    for row in mat:
        for item in row:
            print(item, end=" ")
        print()


def print_color_matrix(mat):
    for row in mat:
        for item in row:
            txtcolor = colors.fg.black
            if item == 're':
                txtcolor = colors.fg.red
            elif item == 'xx':
                item = "  "
            print(txtcolor, item, end="")
        print()


def car_coordinates(car, position):
    res = []
    for i in range(car.length):
        res.append((position[0] + i * car.is_vertical, position[1] + i * (not car.is_vertical)))
    return res


def main():
    while True:
        selected_level = input("Please choose a level: \n"
                               "A = beginner\nB = intermediate\nC = advanced"
                               "\nD = expert\n").upper()
        if selected_level == "A":
            import example_board_beginner
            start_board = Board(example_board_beginner.board_dict, 6, None, "Begin")
        elif selected_level == "B":
            import example_board_intermediate
            start_board = Board(example_board_intermediate.board_dict, 6, None, "Begin")
        elif selected_level == "C":
            import example_board_advanced
            start_board = Board(example_board_advanced.board_dict, 6, None, "Begin")
        elif selected_level == "D":
            import example_board_expert
            start_board = Board(example_board_expert.board_dict, 6, None, "Begin")
        else:
            print("invalid input")
            continue
        x0 = time.perf_counter()
        solve_game.solve(start_board)
        x1 = time.perf_counter()
        print("took {} seconds".format(x1 - x0))
        break


if __name__ == '__main__':
    main()

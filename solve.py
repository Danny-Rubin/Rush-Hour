from rush_hour_main import *

def is_solved(board, n):
    car_front_pos = forward(board.red_car_pos, "right", RED_CAR_LEN-1)
    vac_mat = board.vacancy_mat()
    while car_front_pos[1] < n - 1:
        if vac_mat[car_front_pos[0]][car_front_pos[1] + 1] == True:
            return False
        car_front_pos = forward(car_front_pos, "right", 1)
    return True

def solve(board_dict, n=6):
    start = Board(board_dict, n)
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


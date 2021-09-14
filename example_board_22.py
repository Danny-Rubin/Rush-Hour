from rush_hour_main import *

light_green = Car(True, "light_green", 2)
yellow = Car(False, "yellow", 3)
orange = Car(True, "orange", 2)
red = Car(False, "red", 2)
light_purple = Car(True, "light purple", 3)
light_blue = Car(False, "light blue", 2)
dark_purple = Car(False, "dark purple", 2)
pink = Car(True, "pink", 2)
dark_green = Car(True, "dark_green", 2, )
black = Car(False, "black", 2)
turquoise = Car(False, "turquoise", 3)
falcon = Car(True, "falcon", 2)
board_dict_22 = {light_green: [0, 2], yellow: [0, 3], orange: [1, 0],
             red: [2,1],light_purple: [1, 3], light_blue: [1, 4], dark_purple: [3, 4],
             pink:[3,1], dark_green:[4, 0], black: [4,2], turquoise:[5,1],
             falcon:[4,5]}
car_list_22 = [light_green, yellow, orange, red, light_purple, light_blue,
            dark_purple, pink, dark_green, black, turquoise, falcon]
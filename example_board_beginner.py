from rush_hour_main import *
# game level 01

light_green = Car(False, "light green", 2)
yellow = Car(True, "yellow", 3)
orange = Car(True, "orange", 2)
red = Car(False, "red", 2)
light_purple = Car(True, "light purple", 3)
light_blue = Car(False, "light blue", 2)
turquoise = Car(False, "turquoise", 3)
dark_blue = Car(True, "dark blue", 3)

board_dict = {light_green: [0, 0], yellow: [0, 5], orange: [4, 0],
             red: [2,1],light_purple: [1, 0], light_blue: [4, 4],
             turquoise:[5,2],
             dark_blue:[1,3]}

# board_dict_01 = { yellow: [0, 5],light_blue: [4, 4],
#              red: [2,1], turquoise:[5,2],
#              dark_blue:[1,3]}

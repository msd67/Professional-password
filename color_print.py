# Python Tutorial
# Created by masoud mahjoubi
# color print

import sys
import os


# windows system coloer
# 0 = Black       8 = Gray
# 1 = Blue        9 = Light Blue
# 2 = Green       A = Light Green
# 3 = Aqua        B = Light Aqua
# 4 = Red         C = Light Red
# 5 = Purple      D = Light Purple
# 6 = Yellow      E = Light Yellow
# 7 = White       F = Bright White

color_Dict = {'Black':'0', 'Blue':'1', 'Green':'2', 'Aqua':'3', 'Red':'4',
                'Puple':'5', 'Yello':'6', 'White':'7', 'Gray':'8', 'Light_Blue':'9', 'Light_Green':'A', 
                'Light_Aqua':'B', 'Light_Red':'C', 'Light_Purple':'D', 'Light_Yellow':'E', 'Bright_White':'F'}

os.system('color ' + color_Dict['White'])

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

    def clear():
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
        
        # for mac and linux (here, os.name is 'posix')
        else:
            _ = os.system('clear')


   
pi = 3.14159265359
pc = 6.62607004

import webbrowser
import colored
from colored import stylize
import sys
import time


error = colored.fg("red") + colored.attr("bold")
green = colored.fg("green_3a") + colored.attr("bold")













          




print(stylize("          _____                    _____          ",green))
print(stylize("         /\    \                  /\    \         ",green))
print(stylize("        /::\    \                /::\    \       ",green))
print(stylize("       /::::\    \              /::::\    \       ",green))
print(stylize("      /::::::\    \            /::::::\    \     ",green))
print(stylize("     /:::/\:::\    \          /:::/\:::\    \    ",green))
print(stylize("    /:::/__\:::\    \        /:::/__\:::\    \   ",green))
print(stylize("   /::::\   \:::\    \      /::::\   \:::\    \   ",green))
print(stylize("  /::::::\   \:::\    \    /::::::\   \:::\    \  ", green))
print(stylize(" /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ ",green))
print(stylize("/:::/  \:::\   \:::\____\/:::/  \:::\   \:::\____\ ",green))
print(stylize("\::/    \:::\  /:::/    /\::/    \:::\   \::/    /",green))
print(stylize(" \/____/ \:::\/:::/    /  \/____/ \:::\   \/____/ ",green))
print(stylize("          \::::::/    /            \:::\    \    ",green))
print(stylize("           \::::/    /              \:::\____\    ",green))
print(stylize("           /:::/    /                \::/    /    ",green))
print(stylize("          /:::/    /                  \/____/     ",green))
print(stylize("         /:::/    /                               ",green))
print(stylize("        /:::/    /                               ",green))
print(stylize("        \::/    /                                ",green))
print(stylize("         \/____/                                 ",green))
print(stylize(" _____ _____ _____ _____ ",green))
print(stylize("|____ |  _  |  _  |  _  |",green))
print(stylize("    / / |/' | |/' | |/' |",green))
print(stylize("    \ \  /| |  /| |  /| |",green))
print(stylize(".___/ | |_/ | |_/ | |_/ /",green))
print(stylize("\____/ \___/ \___/ \___/",green))


print("1. Calculator - Calculator")
print("2. TTT/TicTacToe - TicTacToe")

ProgramChoice = input("What do you want to do?")
print("Input your sum")
sum = input("")


if "*" in sum:
    operator = "*"
if "+" in sum:
    operator = "+"
if "-" in sum:
    operator = "-"
if "/" in sum:
    operator = "/"
    
print(operator)


sum = sum.replace("*", "")
sum = sum.replace("/", "")
sum = sum.replace("+", "")
sum = sum.replace("-", "")


sum = sum.replace("*", "")
sum = sum.replace("/", "")
sum = sum.replace("+", "")
sum = sum.replace("-", "")



s1 = sum[:len(sum)//2]
s2 = sum[len(sum)//2:]

sum = int(sum)
print(s1*s2)


print("")
print("")
print("")
print("Made by AverageAxe and JWG")
print("V1.0 - Pre-Release")
input("Press enter to exit to desktop") 

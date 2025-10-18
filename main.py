from my_module import greet_from_sebastian, VERSION, another_greet
from math import sqrt
import sys
from utlis import my_tools
# import my_module


# my_module.greet_from_sebastian()
# print(my_module.VERSION)

print(VERSION)
greet_from_sebastian()
another_greet("Kurt")

if __name__ == "__main__":
    print(sqrt(9))
    print(sys.path)
    my_tools.my_tool()

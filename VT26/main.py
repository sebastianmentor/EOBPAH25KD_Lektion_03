import math
from my_module import calculate_distance, another_function_in_my_module, my_module2
import utils
import utils.helpers
import sys
import os
# import my_module

MODULE_PATH: str = "./my_module.py"


def sqrt_and_add(num1: int, num2:int):
    return math.sqrt(num1) + math.sqrt(num2)


def run():
    print("Do some math! Only positive integers are allowed!")
    while True:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        if num1.isdigit() and num2.isdigit():
            print(sqrt_and_add(int(num1), int(num2)))

        else:
            print("Hey, we said integers as input right?")

        
        if (input("Continue (y/n)").lower() == "n"): break

if __name__=="__main__":
    print("In file main.py and __name__ is", __name__)
    print(calculate_distance((0,0), (5,5)))
    another_function_in_my_module()
    my_module2.func2()
    utils.helpers.help1()
    print(sys.path)
    if os.path.exists(MODULE_PATH):
        print("File exist!")
    # run()
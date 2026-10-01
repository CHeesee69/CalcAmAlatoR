import os
import math
from sympy import symbols, Eq, solve

def main():
    print("")
    print("You have selected Basic trigonometry.")
    print("Please enter your equation in the format: sin(x), cos(x), tan(x), csc(x), sec(x), cot(x) without spaces or parentheses.")
    print("enter your equation:")
    equation = input()
    print("")
    print(equation + " = " + str(eval(equation)))
    print("")
    print("press enter to continue")
    input()


if __name__ == "__main__":
    main()
from operator import eq
import os
import math
from sympy import solve

def main():
    print("")
    print("You have selected Basic Arithmatic.")
    print("Please enter your equation in the format ")
    print("enter your equation:")
    equation = input()
    print("")
    print("The answer to your equation is: " + str(eval(equation)))
    print("")
    print("Press A to continue evaluating this string")
    continue = input()
        if eq(continue, "A") or eq(continue, "a"):
                    main()
    

if __name__ == "__main__":
    main()
    
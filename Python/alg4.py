import os
import math
import sympy as sp
def main():
    print("")
    print("You have selected Basic Algebra.")
    print("Please enter the number of different variables in your equation:")
    num_vars = int(input())
    print("")
    print("What would you like to calculate?")
    print("1. Solve for variables")
    print("2. Simplify expression")
    print("3. Factor expression")
    print("4. Expand expression")
    print("5. Back to main menu")
    choice = int(input())
    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("Invalid input. Please enter a number between 1 and 5.")
    if choice == 1:
        print("You have selected Solve for variables.")
        print("Please enter your equation in the format: ax + by + c, 0 where the comma is the equals sign.")
        print("enter your equation:")
        equation = input()
        print("")
        print("Please enter the variable you want to solve for:")
        variable = input()
        print("")
        x = sp.symbols(variable)
        eq = sp.sympify(equation)
        solution = sp.solve(eq, x)
        print("The solution for " + variable + " is: " + str(solution))
    elif choice == 2:
        print("You have selected Simplify expression.")
        print("Please enter your equation in the format: ax + by + c, 0 where the comma is the equals sign.")
        print("enter your expression:")
        expression = input()
        print("")
        simplified_expression = sp.simplify(expression)
        print("The simplified expression is: " + str(simplified_expression))
    elif choice == 3:
        print("You have selected Factor expression.")
        print("Please enter your equation in the format: ax + by + c, 0 where the comma is the equals sign.")
        print("enter your expression:")
        expression = input()
        print("")
        factored_expression = sp.factor(expression)
        print("The factored expression is: " + str(factored_expression))
    elif choice == 4:
        print("You have selected Expand expression.")
        print("Please enter your equation in the format: (ax + by), (dx + ey), etc. without spaces or parentheses.")
        print("enter your expression:")
        expression = input()
        print("")
        expanded_expression = sp.expand(expression)
        print("The expanded expression is: " + str(expanded_expression))
    elif choice == 5:
        return
    print("press enter to continue")
    input()
if __name__ == "__main__":
    main() 
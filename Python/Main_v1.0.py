import math
import os
import geo2
import arth1
import trig3
import alg4
while True:
    print("CalcAmAlatoR v1.0")
    print("")
    print("What would you like to calculate?")
    print("")
    print("1. Basic Arithmatic")
    print("2. Geometric Shapes")
    print("3. Trigonometry")
    print("4. Algebra")
    print("5. exit")
    type = input("Enter the number corresponding to your choice: ")
    if type != "1" and type != "2" and type != "3" and type != "4" and type != "5":
        print("Invalid input. Please enter a number between 1 and 5.")
    if type == "1":
        arth1.main()
    elif type == "2":
        geo2.main()
    elif type == "3":
        trig3.main()
    elif type == "4":
        alg4.main()
    elif type == "5":
        print("Exiting the program.")
        break
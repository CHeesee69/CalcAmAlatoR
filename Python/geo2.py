import os
import math
from secrets import choice
def main():
    print("")
    print("You have selected Geometric Shapes.")
    print("Please select what you want to calculate:")
    print("")
    print("1. Area")
    print("2. Perimeter")
    print("3. Volume")
    print("4. Surface Area")
    print("5. Back to main menu")
    print("")
    choice = input("Enter the number corresponding to your choice: ")
    print("")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("Invalid input. Please enter a number between 1 and 5.")
    if choice == "1":
        print("You have selected Area.")
        print("")
        print("Please select the shape you want to calculate the area for:")
        print("")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Back to main menu")
        print("")
        shape = input("Enter the number corresponding to your choice: ")
        print("")
        if shape != "1" and shape != "2" and shape != "3" and shape != "4" and shape != "5":
            print("Invalid input. Please enter a number between 1 and 5.")
        if shape == "1":
            print("You have selected Square.")
            side = float(input("Please enter the length of one side of the square: "))
            area = side * side
            print("The area of the square is: " + str(area))
        if shape == "2":
            print("You have selected Rectangle.")
            length = float(input("Please enter the length of the rectangle: "))
            width = float(input("Please enter the width of the rectangle: "))
            area = length * width
            print("The area of the rectangle is: " + str(area))
        if shape == "3":
            print("You have selected Triangle.")
            base = float(input("Please enter the base of the triangle: "))
            height = float(input("Please enter the height of the triangle: "))
            area = 0.5 * base * height
            print("The area of the triangle is: " + str(area))
        if shape == "4":
            print("You have selected Circle.")
            radius = float(input("Please enter the radius of the circle: "))
            area = math.pi * radius * radius
            print("The area of the circle is: " + str(area))
        if shape == "5":
            print("Returning to main menu.")
            exec(open("Main.py").read())
    if choice == "2":
        print("You have selected Perimeter.")
        print("Please select the shape you want to calculate the perimeter for:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Back to main menu")
        shape = input("Enter the number corresponding to your choice: ")
        if shape != "1" and shape != "2" and shape != "3" and shape != "4" and shape != "5":
            print("Invalid input. Please enter a number between 1 and 5.")
        if shape == "1":
            print("You have selected Square.")
            side = float(input("Please enter the length of one side of the square: "))
            perimeter = 4 * side
            print("The perimeter of the square is: " + str(perimeter))
        if shape == "2":
            print("You have selected Rectangle.")
            length = float(input("Please enter the length of the rectangle: "))
            width = float(input("Please enter the width of the rectangle: "))
            perimeter = 2 * (length + width)
            print("The perimeter of the rectangle is: " + str(perimeter))
        if shape == "3":
            print("You have selected Triangle.")
            side1 = float(input("Please enter the length of the first side of the triangle: "))
            side2 = float(input("Please enter the length of the second side of the triangle: "))
            side3 = float(input("Please enter the length of the third side of the triangle: "))
            perimeter = side1 + side2 + side3
            print("The perimeter of the triangle is: " + str(perimeter))
        if shape == "4":
            print("You have selected Circle.")
            radius = float(input("Please enter the radius of the circle: "))
            perimeter = 2 * math.pi * radius
            print("The circumference of the circle is: " + str(perimeter))
        if shape == "5":
            print("Returning to main menu.")
            exec(open("Main.py").read())
    if choice == "3":
        print("You have selected Volume.")
        print("Please select the shape you want to calculate the volume for:")
        print("1. Cube")
        print("2. Rectangular Prism")
        print("3. Sphere")
        print("4. Cylinder")
        print("5. Cone")
        print("6. Back to main menu")
        shape = input("Enter the number corresponding to your choice: ")
        if shape != "1" and shape != "2" and shape != "3" and shape != "4" and shape != "5" and shape != "6":
            print("Invalid input. Please enter a number between 1 and 6.")
        if shape == "1":
            print("You have selected Cube.")
            side = float(input("Please enter the length of one side of the cube: "))
            volume = side * side * side
            print("The volume of the cube is: " + str(volume))
        if shape == "2":
            print("You have selected Rectangular Prism.")
            length = float(input("Please enter the length of the rectangular prism: "))
            width = float(input("Please enter the width of the rectangular prism: "))
            height = float(input("Please enter the height of the rectangular prism: "))
            volume = length * width * height
            print("The volume of the rectangular prism is: " + str(volume))
        if shape == "3":
            print("You have selected Sphere.")
            radius = float(input("Please enter the radius of the sphere: "))
            volume = (4/3) * math.pi * radius * radius * radius
            print("The volume of the sphere is: " + str(volume))
        if shape == "4":
            print("You have selected Cylinder.")
            radius = float(input("Please enter the radius of the cylinder: "))
            height = float(input("Please enter the height of the cylinder: "))
            volume = math.pi * radius * radius * height
            print("The volume of the cylinder is: " + str(volume))
        if shape == "5":
            print("You have selected Cone.")
            radius = float(input("Please enter the radius of the cone: "))
            height = float(input("Please enter the height of the cone: "))
            volume = (1/3) * math.pi * radius * radius * height
            print("The volume of the cone is: " + str(volume))
        if shape == "6":
            print("Returning to main menu.")
            exec(open("Main.py").read())
    if choice == "4":
        print("You have selected Surface Area.")
        print("Please select the shape you want to calculate the surface area for:")
        print("1. Cube")
        print("2. Rectangular Prism")
        print("3. Sphere")
        print("4. Cylinder")
        print("5. Cone")
        print("6. Back to main menu")
        shape = input("Enter the number corresponding to your choice: ")
        if shape != "1" and shape != "2" and shape != "3" and shape != "4" and shape != "5" and shape != "6":
            print("Invalid input. Please enter a number between 1 and 6.")
        if shape == "1":
            print("You have selected Cube.")
            side = float(input("Please enter the length of one side of the cube: "))
            surface_area = 6 * side * side
            print("The surface area of the cube is: " + str(surface_area))
        if shape == "2":
            print("You have selected Rectangular Prism.")
            length = float(input("Please enter the length of the rectangular prism: "))
            width = float(input("Please enter the width of the rectangular prism: "))
            height = float(input("Please enter the height of the rectangular prism: "))
            surface_area = 2 * (length * width + length * height + width * height)
            print("The surface area of the rectangular prism is: " + str(surface_area))
        if shape == "3":
            print("You have selected Sphere.")
            radius = float(input("Please enter the radius of the sphere: "))
            surface_area = 4 * math.pi * radius * radius
            print("The surface area of the sphere is: " + str(surface_area))
        if shape == "4":
            print("You have selected Cylinder.")
            radius = float(input("Please enter the radius of the cylinder: "))
            height = float(input("Please enter the height of the cylinder: "))
            surface_area = 2 * math.pi * radius * (radius + height)
            print("The surface area of the cylinder is: " + str(surface_area))
        if shape == "5":
            print("You have selected Cone.")
            radius = float(input("Please enter the radius of the cone: "))
            height = float(input("Please enter the height of the cone: "))
            surface_area = math.pi * radius * (radius + math.sqrt(height * height + radius * radius))
            print("The surface area of the cone is: " + str(surface_area))
        if shape == "6":
            print("Returning to main menu.")

    if choice == "5":
        print("Returning to main menu.")
    print("press enter to continue")
    input()

if __name__ == "__main__":
    main()

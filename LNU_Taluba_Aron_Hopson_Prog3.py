# Name : Taluba Aron Hopson
# Student ID : 101747537
# Date : 3rd October 2023

'''This Python program, named `LNU_Taluba_Aron_Hopson_Prog3.py`, demonstrates modularization and functional 
decomposition to calculate the area and perimeter/circumference of various geometric shapes.
It starts by greeting the user and explaining its purpose. The program utilizes a separate
module called `shapes.py`, which contains functions for calculating the area and perimeter 
of at least three geometric shapes.

The program presents a menu to the user in a loop, allowing them to choose from options like 
Rectangle, Circle, Triangle, or Exit. It displays the relevant formulas for each shape and
prompts the user for the required dimensions. Upon receiving user input, it invokes the functions
from the `shapes.py` module to perform the calculations and then displays the results.

The code is modularized with functions for menu presentation, user choice processing,
and result display, each with its own documentation. Comments throughout the code provide 
clarity and understanding. The program ensures a meaningful and complete interaction with the user.
It gracefully exits when the user chooses to exit from the menu.'''

# importing the functions from shapes.py
from shapes import calculate_circle_area
from shapes import calculate_circle_perimeter
from shapes import calculate_rectangle_area
from shapes import calculate_rectangle_perimeter
from shapes import calculate_triangle_area
from shapes import calculate_triangle_perimeter

def display_menu():
    """Display the main menu."""
    print("1. Calculate Circle")
    print("2. Calculate Rectangle")
    print("3. Calculate Triangle")
    print("4. Exit")


def process_choice(choice):
    """
    Process the user's choice and calculate area/perimeter accordingly.

    Args:
        choice (str): The user's menu choice.
    """
    if choice == "1":
        print("Formula for Area of Circle: π * radius^2")
        print("Formula for Perimeter of a Circle: 2 * π * radius")
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        perimeter = calculate_circle_perimeter(radius)
    elif choice == "2":
        print("Formula for Area of a Rectangle: length * width")
        print("Formula for Perimeter of a Rectangle: 2 * (length + width)")
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        perimeter = calculate_rectangle_perimeter(length, width)
    elif choice == "3":
        print("Formula for Area of a Triangle: 0.5 * base * height")
        print("Formula for Perimeter of a Triangle: side1 + side2 + side3")
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice! Please select a valid option.")
        return

    display_results(area, perimeter)


def display_results(area, perimeter):
    """
    Display the calculated area and perimeter.

    Args:
        area (float): The calculated area.
        perimeter (float): The calculated perimeter.
    """
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


def exit_program():
    """Exit the program."""
    print("Thank you for using the Geometry Calculator. Goodbye!")
    exit()


def main():
    
    user_name = input("Please Enter your name : ")
    print(f"\nWelcome {user_name} to the Geometry Calculator!")
    while True:
        
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        process_choice(choice)


if __name__ == "__main__":
    main()

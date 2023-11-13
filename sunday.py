# # def triangle():
# #     val = int(input("enter: "))
# #     c =0
# #     for i in range(val):
# #         for j in range(i+1):
# #             print(c, end=" ")
# #             c += 1
# #         print()    
    
# # def rectangle_filled():
# #     h = int(input("enter h"))
# #     w = int(input("enter w"))
    
# #     for i in range(h):
# #         c=0
# #         for j in range(w):
# #             if i == 0 or i == h - 1 or j == 0 or j == w - 1:
# #                 print(c, end=" ")
# #                 c += 1
# #             else:
# #                 print(" ", end=" ")    
# #         print() 
        
# def pyramid():
#     h = int(input("enter h"))
#     c_num = 1
#     for i in range(1,h+1):
#         for j in range(h-i):
#             print(" ",end=" ")
#         for k in range(2 * i - 1):
#             print(c_num,end=" ")
#             c_num +=1    
#         print()    
           
# def main():

#     # triangle()
#     # rectangle_filled()
#     pyramid()

# if __name__ =="__main__":
#     main()
    
    
# def pyramid():
#     h = int(input("Enter the height of the pyramid: "))
#     max_num = h * h  # Calculate the maximum number to be printed
#     width = len(str(max_num))  # Calculate the width needed for alignment

#     current_num = 1
#     for i in range(1, h + 1):
#         for _ in range(h - i):
#             print(" " * width, end=" ")  # Adjust alignment based on width
#         for _ in range(2 * i - 1):
#             num_str = str(current_num).rjust(width)  # Right-align the number
#             print(num_str, end=" ")
#             current_num += 1
#         print()

# def main():
#     pyramid()

# if __name__ == "__main__":
#     main()
    
    
# shapes.py module
import math

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius**2

def calculate_circle_circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * math.pi * radius

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def calculate_triangle_perimeter(side1, side2, side3):
    """Calculate the perimeter of a triangle."""
    return side1 + side2 + side3


def main():
    print("Welcome to the Geometry Calculator!")

    while True:
        print("\nMenu:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Exit")

        choice = input("Please select a shape (1/2/3/4): ")

        if choice == '1':
            print("\nRectangle:")
            print("Formula for Area: length * width")
            print("Formula for Perimeter: 2 * (length + width)")
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
            perimeter = calculate_rectangle_perimeter(length, width)
        elif choice == '2':
            print("\nCircle:")
            print("Formula for Area: π * radius^2")
            print("Formula for Circumference: 2 * π * radius")
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
            perimeter = calculate_circle_circumference(radius)
        elif choice == '3':
            print("\nTriangle:")
            print("Formula for Area: 0.5 * base * height")
            print("Formula for Perimeter: side1 + side2 + side3")
            side1 = float(input("Enter the length of side 1 of the triangle: "))
            side2 = float(input("Enter the length of side 2 of the triangle: "))
            side3 = float(input("Enter the length of side 3 of the triangle: "))
            area = calculate_triangle_area(side1, side2)
            perimeter = calculate_triangle_perimeter(side1, side2, side3)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print("\nShape: ")
        if choice == '1':
            print("Rectangle")
        elif choice == '2':
            print("Circle")
        elif choice == '3':
            print("Triangle")
        print("Area:", area)
        print("Perimeter/Circumference:", perimeter)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
    
    
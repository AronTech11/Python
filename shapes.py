import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius**2


def calculate_circle_perimeter(radius):
    """
    Calculate the perimeter (circumference) of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The perimeter (circumference) of the circle.
    """
    return 2 * math.pi * radius


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


def calculate_rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return 2 * (length + width)


def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height


def calculate_triangle_perimeter(side1, side2, side3):
    """
    Calculate the perimeter of a triangle.

    Args:
        side1 (float): Length of side 1.
        side2 (float): Length of side 2.
        side3 (float): Length of side 3.

    Returns:
        float: The perimeter of the triangle.
    """
    return side1 + side2 + side3
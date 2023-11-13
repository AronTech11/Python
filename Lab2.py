# # # # Name = Taluba Aron Hopson
# # # # Student ID = 101747537

# # # '''Calculating the area of circle'''


# # # def Area_of_Cicle(Radius_of_Circle):
# # #     Value_of_PI = 22/7
# # #     area_of_cicle = Value_of_PI*Radius_of_Circle*Radius_of_Circle
# # #     return area_of_cicle


# # # def main():
# # #     Radius_of_Circle = float(input("Enter the raduis of a circle : "))  # input
# # #     print("Area of a circle is :", Area_of_Cicle(Radius_of_Circle))  # output


# # # if __name__ == "__main__":
# # #     main()


# # # '''Calculating the area of Rectangle'''


# # # def Area_of_Rectangle(Length_of_Rectangle, Width_of_Rectangle):
# # #     area_of_rectangle = Length_of_Rectangle*Width_of_Rectangle
# # #     return area_of_rectangle


# # # def main():

# # #     Width_of_Rectangle = float(
# # #         input("Enter the Width of a Rectangle in Metre: "))  # Input
# # #     Length_of_Rectangle = float(
# # #         input("Enter the Length of a Rectangle in Metre: "))  # Input

# # #     if (Width_of_Rectangle > 0 and Length_of_Rectangle > 0):  # Output using the conditions
# # #         print("Area of a circle is :", Area_of_Rectangle(
# # #             Length_of_Rectangle, Width_of_Rectangle))
# # #     else:
# # #         print("Wrong input")


# # # if __name__ == "__main__":
# # #     main()


# # # def main():
# # #     print("1 Area of a circle")
# # #     print("2 Area of a rectangle")

# # #     option = input()

# # #     if (option == "1"):
# # #         Radius_of_Circle = float(
# # #             input("Enter the raduis of a circle : "))  # input
# # #         print("Area of a circle is :", Area_of_Cicle(Radius_of_Circle))  # output
# # #     elif (option == "2"):
# # #         Width_of_Rectangle = float(
# # #             input("Enter the Width of a Rectangle in Metre: "))  # Input
# # #         Length_of_Rectangle = float(
# # #             input("Enter the Length of a Rectangle in Metre: "))  # Input

# # #         if (Width_of_Rectangle > 0 and Length_of_Rectangle > 0):  # Output using the conditions
# # #             print("Area of a Rectangle is :", Area_of_Rectangle(
# # #                 Length_of_Rectangle, Width_of_Rectangle))
# # #         else:
# # #             print("Wrong input")


# # # if __name__ == "__main__":
# # #     main()


# # def Area_of_Cicle(Radius_of_Circle):
# #     Value_of_PI = 22/7
# #     area_of_cicle = Value_of_PI*Radius_of_Circle*Radius_of_Circle
# #     return area_of_cicle


# # '''Calculating the area of Rectangle'''


# # def Area_of_Rectangle(Length_of_Rectangle, Width_of_Rectangle):
# #     area_of_rectangle = Length_of_Rectangle*Width_of_Rectangle
# #     return area_of_rectangle


# # def main():
# #     print("1 Area of a circle")
# #     print("2 Area of a rectangle")

# #     option = input()

# #     if (option == "1"):
# #         Radius_of_Circle = float(
# #             input("Enter the raduis of a circle : "))  # input
# #         print("Area of a circle is :", Area_of_Cicle(Radius_of_Circle))  # output
# #     elif (option == "2"):
# #         Width_of_Rectangle = float(
# #             input("Enter the Width of a Rectangle in Metre: "))  # Input
# #         Length_of_Rectangle = float(
# #             input("Enter the Length of a Rectangle in Metre: "))  # Input

# #         if (Width_of_Rectangle > 0 and Length_of_Rectangle > 0):  # Output using the conditions
# #             print("Area of a Rectangle is :", Area_of_Rectangle(
# #                 Length_of_Rectangle, Width_of_Rectangle))
# #         else:
# #             print("Wrong input")


# # if __name__ == "__main__":
# #     main()


# # some more functions
# # def is_prime(n):
# # 	if n in [2, 3]:
# # 		return True
# # 	if (n == 1) or (n % 2 == 0):
# # 		return False
# # 	r = 3
# # 	while r * r <= n:
# # 		if n % r == 0:
# # 			return False
# # 		r += 2
# # 	return True
# # print(is_prime(8), is_prime(79))


# # def simpleGeneratorFun():
# #     yield 1
# #     yield 2
# #     yield 3
 
 
# # # Driver code to check above generator function
# # for value in simpleGeneratorFun():
# #     print(value)
	
# # filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
# # print("filter_nums():", filter_nums("Geeks101"))
 
# # do_exclaim = lambda s: s + '!'
# # print("do_exclaim():", do_exclaim("I am tired"))
 
# # find_sum = lambda n: sum([int(x) for x in str(n)])
# # print("find_sum():", find_sum(101))


# # class Dog:

# # 	# class attribute
# # 	attr1 = "mammal"

# # 	# Instance attribute
# # 	def __init__(self, name):
# # 		self.name = name

# # # Driver code
# # # Object instantiation
# # Rodger = Dog("Ro vger")
# # Tommy = Dog("Tommy")

# # # Accessing class attributes
# # print("Rodger is a {}".format(Rodger.__class__.attr1))
# # print("Tommy is also a {}".format(Tommy.__class__.attr1))

# # # Accessing instance attributes
# # print("My name is {}".format(Rodger.name))
# # print("My name is {}".format(Tommy.name))


# import random

# class Matrix:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.matrix = [[random.randint(0, 255) for _ in range(width)] for _ in range(height)]

#     def get_maximum_value(self):
#         max_val = -1
#         for row in self.matrix:
#             max_val = max(max_val, max(row))
#         return max_val

#     def get_maximum_index(self):
#         max_val = self.get_maximum_value()
#         for i, row in enumerate(self.matrix):
#             if max_val in row:
#                 j = row.index(max_val)
#                 return (i, j)

#     def get_minimum_value(self):
#         min_val = 256  # Initialize with a value greater than 255
#         for row in self.matrix:
#             min_val = min(min_val, min(row))
#         return min_val

#     def get_minimum_index(self):
#         min_val = self.get_minimum_value()
#         for i, row in enumerate(self.matrix):
#             if min_val in row:
#                 j = row.index(min_val)
#                 return (i, j)

#     def transpose(self):
#         transposed_matrix = [[self.matrix[j][i] for j in range(self.height)] for i in range(self.width)]
#         self.matrix = transposed_matrix
#         self.height, self.width = self.width, self.height

#     def get_size(self):
#         return (self.height, self.width)

# if __name__ == "__main__":
#     height = int(input("Enter the height of the matrix: "))
#     width = int(input("Enter the width of the matrix: "))
    
#     matrix = Matrix(height, width)
    
#     print("Matrix:")
#     for row in matrix.matrix:
#         print(row)
    
#     print(f"Maximum Value: {matrix.get_maximum_value()}")
#     print(f"Maximum Value Index: {matrix.get_maximum_index()}")
    
#     print(f"Minimum Value: {matrix.get_minimum_value()}")
#     print(f"Minimum Value Index: {matrix.get_minimum_index()}")
    
#     print("Transposing the matrix...")
#     matrix.transpose()
    
#     print("Transposed Matrix:")
#     for row in matrix.matrix:
#         print(row)
    
#     print(f"Matrix Size (Height, Width): {matrix.get_size()}")

import re

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.words = []

class WordExtractor:
    def __init__(self, text):
        self.text = text
        self.root = None

    def insert_word(self, word):
        if not word:
            return

        if not self.root:
            self.root = TreeNode(word[0])

        if word[0] == self.root.value:
            return

        self._insert_recursive(self.root, word, "root")

    def _insert_recursive(self, node, word, position):
        if not word:
            return

        if word[0] < node.value:
            if node.left is None:
                node.left = TreeNode(word[0])
            self._insert_recursive(node.left, word, "left")
        elif word[0] > node.value:
            if node.right is None:
                node.right = TreeNode(word[0])
            self._insert_recursive(node.right, word, "right")
        else:
            node.words.append((position, word))

    def extract_words(self):
        pattern_split = r'\s'
        words = re.split(pattern_split, self.text)
        for word in words:
            self.insert_word(word)
        return self.root

    def traverse_tree(self, node):
        if node:
            self.traverse_tree(node.left)
            for position, word in node.words:
                print(f"{node.value} ({position}): {word}")
            self.traverse_tree(node.right)

def main():
    INPUT_STRING = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum Ipsum passages,and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"""


    word_extractor = WordExtractor(INPUT_STRING)
    root_node = word_extractor.extract_words()

    print("Traversing the tree structure:")
    word_extractor.traverse_tree(root_node)

if __name__ == "__main__":
    main()

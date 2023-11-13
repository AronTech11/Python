
# ''' write a program to count a number of vowels in a string of 100 words
#   example output : {a:10,e:13,i:10,o:9,u:12}'''


# def count_vowels(input_string, vowels):
#     # Initialize a dictionary to store vowel counts
#     vowel_counts = {vowel: 0 for vowel in vowels}

#     # Convert the input string to lowercase for case-insensitive counting
#     input_string = input_string.lower()

#     # Loop through each character in the input string
#     for char in input_string:
#         # Check if the character is a vowel
#         if char in vowels:
#             # Increment the count for that vowel
#             vowel_counts[char] += 1

#     return vowel_counts


# def main():
#     # Define the input string
#     input_string = """
#     Lorem Ipsum is simply dummy text of the printing and typesetting industry.
#     Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
#     when an unknown printer took a galley of type and scrambled it to make a type
#     specimen book. It has survived not only five centuries, but also the leap into
#     electronic typesetting, remaining essentially unchanged. It was popularised in
#     the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
#     and more recently with desktop publishing software like Aldus PageMaker including
#     versions of Lorem Ipsum.
#     """

#     # Define the list of vowels
#     vowels = ['a', 'e', 'i', 'o', 'u']

#     # Call the function to count vowels
#     vowel_counts = count_vowels(input_string, vowels)

#     # Print the vowel counts
#     print(vowel_counts)


# if __name__ == "__main__":
#     main()


# if any letter is equal to the root node eliminate the letter found

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
   
    input_string = INPUT_STRING.lower()
    
    word_extractor = WordExtractor(input_string)
    root_node = word_extractor.extract_words()

    print("Traversing the tree structure:")
    word_extractor.traverse_tree(root_node)

if __name__ == "__main__":
    main()

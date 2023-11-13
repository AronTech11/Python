# Name = Taluba Aron Hopson
# Student ID = 101747537

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

        self.insert_recursive(self.root, word, "root")

    def insert_recursive(self, node, word, position):
        if not word:
            return

        if word[0] < node.value:
            if node.left is None:
                node.left = TreeNode(word[0])
            self.insert_recursive(node.left, word, "left")
        elif word[0] > node.value:
            if node.right is None:
                node.right = TreeNode(word[0])
            self.insert_recursive(node.right, word, "right")
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
    INPUT_STRING = """xorem Ipsum is simply dummy text of """

    word_extractor = WordExtractor(INPUT_STRING)
    root_node = word_extractor.extract_words()

    print("Traversing the tree structure:")
    word_extractor.traverse_tree(root_node)

if __name__ == "__main__":
    main()

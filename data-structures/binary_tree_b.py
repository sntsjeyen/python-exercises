'''

File Name: binary_tree_b.py
Author: Jun Nathan Santos
Date Created: 2022-09-12
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Assign the nodes of the given tree and display the nodes:
        8  4  12  2  6  1  3  5  7  10  14  9  11  13  15

'''

# Create the Node class and construct a node.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data
    def print_tree(self): # Print the nodes of the binary tree.
        if self.left:
            self.left.print_tree()
        print(self.node, end = ' ')
        if self.right:
            self.right.print_tree()

# Assign the root of the binary tree.
root = Node(8)

# Assign the left nodes.
root.left = Node(4)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.left.right = Node(3)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(7)

# Assign the right nodes.
root.right = Node(12)
root.right.left = Node(10)
root.right.left.left = Node(9)
root.right.left.right = Node(11)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.right.right.right = Node(15)

# Call the print_tree function to display the nodes.
root.print_tree()
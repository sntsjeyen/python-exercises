'''

File Name: binary_tree_c.py
Author: Jun Nathan Santos
Date Created: 2022-09-19
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a binary tree program from the given data:
        60  45  90  12  53  74  25  99  10  18  30  84  3  82  20  81
    - Display the output in post order traversal technique.

'''

# Create the class that represents the node.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data

# Create the function that displays the nodes in postorder
def display_postorder(root):
    if root:
        display_postorder(root.left)
        display_postorder(root.right)
        print(root.node, end = ' ')

# Assign the root.
root = Node(60)

# Assign the nodes on the root's left side.
root.left = Node(45)
root.left.left = Node(12)
root.left.left.left = Node(10)
root.left.left.left.left = Node(3)
root.left.left.right = Node(25)
root.left.left.right.left = Node(18)
root.left.left.right.left.right = Node(20)
root.left.left.right.right = Node(30)
root.left.right = Node(53)

# Assign the nodes on the root's right side.
root.right = Node(90)
root.right.left = Node(74)
root.right.left.right = Node(84)
root.right.left.right.left = Node(82)
root.right.left.right.left.left = Node(81)
root.right.right = Node(99)

# Display the nodes in postorder by calling the function display_postorder.
display_postorder(root)

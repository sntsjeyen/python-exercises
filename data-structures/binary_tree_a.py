'''

File Name: binary_tree_a.py
Authors: Aljon James Pacheco, Jun Nathan Santos
Date Created: 2022-09-18
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Create a menu with the following options:
        [1] Pre Order
        [2] In Order
        [3] Post Order
        [4] Level Order
        [5] Exit
    - Apply the traversal technique based on the choice of user given this sequence of nodes:
        35  10  75  40  18  45  8  38  9  80  43  50  6  15  28  55  46
    - Display the nodes after every choice.

'''

# Create the Node class and construct a node.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data

# Create the function that performs preorder tree traversal.
def pre_order(root):
    if root:
        print(root.node, end = ' ')
        pre_order(root.left)
        pre_order(root.right)

# Create the function that performs inorder tree traversal.
def in_order(root):
    if root:
        in_order(root.left)
        print(root.node, end = ' ')
        in_order(root.right)

# Create the function that performs postorder tree traversal.
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.node, end = ' ')

# Create the function that performs level order tree traversal.
def level_order(root):
    lvl_order = []
    lvl_order.append(root)
    while(len(lvl_order) > 0):
        print(lvl_order[0].node, end = ' ')
        node = lvl_order.pop(0)
        if node.left is not None:
            lvl_order.append(node.left)
        if node.right is not None:
            lvl_order.append(node.right)
        
# Create the function that represents the set of options.
def options(root):
    choice = 1
    try:
        while choice != 5:
            print('\n\nMenu\n   [1] Preorder\n   [2] Inorder\n   [3] Postorder\n   [4] Level Order\n   [5] Exit')
            choice = int(input('\nEnter your choice : '))
            if choice == 1:
                pre_order(root)
            elif choice == 2:
                in_order(root)
            elif choice == 3:
                post_order(root)
            elif choice == 4:
                level_order(root)
            elif (choice <= 0) or (choice >= 6):
                print('Invalid. Try again.', end = ' ')
    except ValueError:
        print('Invalid. Try again.', end = ' ')
        options(root)

# Assign the root of the binary tree.
root = Node(35)

# Assign the nodes on the left.
root.left = Node(10)
root.left.left = Node(8)
root.left.left.left = Node(6)
root.left.left.right = Node(9)
root.left.right = Node(18)
root.left.right.left = Node(15)
root.left.right.right = Node(28)

# Assign the nodes on the right.
root.right = Node(75)
root.right.left = Node(40)
root.right.left.left = Node(38)
root.right.left.right = Node(45)
root.right.left.right.left = Node(43)
root.right.left.right.right = Node(50)
root.right.left.right.right.left = Node(46)
root.right.left.right.right.right = Node(55)
root.right.right = Node(80)

# Call the options function and let the user choose a traversal operation.
print('\nBinary Tree Nodes: 35 10 75 40 18 45 8 38 9 80 43 50 6 15 28 55 46', end = ' ')
options(root)
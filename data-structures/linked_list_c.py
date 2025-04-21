'''

File Name: linked_list_c.py
Author: Jun Nathan Santos
Date Created: 2022-09-19
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a linked list program that would sort the given data in ascending order (alphabetical):
        F1	| Kiwi
        F2	| Grapes
        F3	| Pineapple
        F4	| Banana
        F5	| Watermelon
        F6	| Apple
        F7	| Strawberry
        F8	| Jackfruit
        F9	| Cherry
        F10 | Orange
    - The word 'FRUITS' is the root to be used.
    - Display the output. 

'''

# Create the class that represents the node.
class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

# Create the class that represents the linked list.
class LinkedList:
    def __init__(self):
        self.head = None
    def display_fruits(self):
        while self.head is not None:
            print(self.head.item)
            self.head = self.head.next

# Assign values to nodes.
fruits = LinkedList()
fruits.head = Node('FRUITS')
F1 = Node('Kiwi')
F2 = Node('Grapes')
F3 = Node('Pineapple')
F4 = Node('Banana')
F5 = Node('Watermelon')
F6 = Node('Apple')
F7 = Node('Strawberry')
F8 = Node('Jackfruit')
F9 = Node('Cherry')
F10 = Node('Orange')

# Link the nodes
fruits.head.next = F6
F6.next = F4
F4.next = F9
F9.next = F2
F2.next = F8
F8.next = F1
F1.next = F10
F10.next = F3
F3.next = F7
F7.next = F5

# Display the nodes in ascending order by calling the function display_fruits.
fruits.display_fruits()
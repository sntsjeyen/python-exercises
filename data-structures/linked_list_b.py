'''

File Name: linked_list_b.py
Author: Jun Nathan Santos
Date Created: 2022-10-08
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that would create a linked list for the given data:
        M1  | M2  | M3  | M4  | M5  | M6  | M7  | M8  | M9  | M10 | M11 | M12
        Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec
    - Assign the node items and node links.
    - Display the linked list items.
    - Given order: Jan -> Jul -> Oct -> Dec -> Feb -> Sep -> May -> Aug -> Nov -> Apr -> Mar -> Jun

'''

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def displayMonths(self):
        while self.head is not None:
            print(self.head.item, end = ' ')
            self.head = self.head.next

months = LinkedList()
months.head = Node('Jan')
M1 = Node('Feb')
M2 = Node('Mar')
M3 = Node('Apr')
M4 = Node('May')
M5 = Node('Jun')
M6 = Node('Jul')
M7 = Node('Aug')
M8 = Node('Sep')
M9 = Node('Oct')
M10 = Node('Nov')
M11 = Node('Dec')

months.head.next = M6
M6.next = M9
M9.next = M11
M11.next = M1
M1.next = M8
M8.next = M4
M4.next = M7
M7.next = M10
M10.next = M3
M3.next = M2
M2.next = M5

months.displayMonths()

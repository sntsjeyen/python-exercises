'''

File Name: linked_list_a.py
Author: Jun Nathan Santos
Date Created: 2022-09-13
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that would create a linked list for the given data
        C1     | C2     | C3     | C4     | C5     | C6     | C7     | C8     | C9     | C10
        Red    | Brown  | Orange | White  | Green  | Yellow | Purple | Blue   | Pink   | Black
    - Include the following options:
        [1] Beginning (Input a new value and add the new node at the beginning of the list)
        [2] End (Input a new value and add the new node at the end of the list)
        [3] In Between (Input a new value and add the new node at the middle of the list)
        [4] Delete (Input an item to remove in the list)
        [5] Display
        [5] Exit
    - Given order: *Color* -> Black -> Blue -> Brown -> Green -> Orange -> Pink -> Purple -> Red -> White -> Yellow

'''

# Create the class that represents each node.
class ColorNode:
    def __init__(c, item = None):
        c.item = item
        c.next = None

# Create the class that represents the linked list.
class ColorsLinkedList:
    def __init__(c):
        c.head = None

    # Create a function that lets the program add the user's inputted color at the beginning.
    def insert_beg(c):
        new_item = input('Enter a color : ')
        new_node = ColorNode(new_item)
        new_node.next = c.head
        c.head = new_node

    # Create a function that lets the program add the user's inputted color at the end.
    def insert_end(c):
        new_item = input('Enter a color : ')
        new_node = ColorNode(new_item)
        if c.head is None:
            c.head = new_node
            return
        last_node = c.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Create a function that lets the program add the user's inputted color in the middle.
    def insert_bet(c):
        new_item = input('Enter a color : ')
        new_node = ColorNode(new_item)
        mid_node = c.head
        length = 0
        check = c.head
        while check is not None:
            length += 1
            check = check.next
        position = int(length / 2)
        for x in range(position):
            mid_node = mid_node.next
        new_node.next = mid_node.next
        mid_node.next = new_node

    # Create a function that lets the program delete the user's inputted color from the list.
    def delete_item(c):
        selected_item = input('Enter a color to remove : ')
        del_node = c.head
        if del_node is not None:
            if del_node.item == selected_item:
                c.head = del_node.next
                del_node = None
                return
        while del_node is not None:
            if del_node.item == selected_item:
                break
            remove = del_node
            del_node = del_node.next
        if del_node == None:
            print(selected_item, 'is not in the list.')
            return
        remove.next = del_node.next
        del_node = None

    # Create a function that lets the program display the colors included in the linked list.
    def display_colors(c):
        display_item = c.head
        print()
        while display_item is not None:
            print(display_item.item)
            display_item = display_item.next

# Create the class and function that represent the menu.
class LinkedListMenu:
    def menu(c):
        choice = 1
        try:
            while choice != 6:
                print('\nMenu\n   [1] Insert at Beginning\n   [2] Insert at End\n   [3] Insert in Between\n   [4] Delete\n   [5] Display\n   [6] Exit')
                choice = int(input('\nEnter your choice : '))
                if choice == 1:
                    ColorsLinkedList.insert_beg(c)              # Call the insert_beg function.
                    ColorsLinkedList.display_colors(c)          # Call the display_colors function.
                elif choice == 2:
                    ColorsLinkedList.insert_end(c)              # Call the insert_end function.
                    ColorsLinkedList.display_colors(c)          # Call the display_colors function.
                elif choice == 3:
                    ColorsLinkedList.insert_bet(c)              # Call the insert_bet function.
                    ColorsLinkedList.display_colors(c)          # Call the display_colors function.
                elif choice == 4:
                    ColorsLinkedList.delete_item(c)             # Call the delete_item function.
                    ColorsLinkedList.display_colors(c)          # Call the display_colors function.
                elif choice == 5:
                    ColorsLinkedList.display_colors(c)          # Call the display_colors function.
                elif choice >= 7:
                    print('Invalid. Try again.')
        except ValueError:
            print('Invalid. Try again.')
            LinkedListMenu.menu(c)
            
# Assign the values for each node.
colors = ColorsLinkedList()
colors.head = ColorNode('*Color*')
C1 = ColorNode('Red')
C2 = ColorNode('Brown')
C3 = ColorNode('Orange')
C4 = ColorNode('White')
C5 = ColorNode('Green')
C6 = ColorNode('Yellow')
C7 = ColorNode('Purple')
C8 = ColorNode('Blue')
C9 = ColorNode('Pink')
C10 = ColorNode('Black')

# Link the nodes.
colors.head.next = C10
C10.next = C8
C8.next = C2
C8.next = C2
C2.next = C5
C5.next = C3
C3.next = C9
C9.next = C7
C7.next = C1
C1.next = C4
C4.next = C6

# Call the menu and let the user choose an operation.
LinkedListMenu.menu(colors)
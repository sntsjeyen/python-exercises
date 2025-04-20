'''

File Name: stack_a.py
Authors: Aljon James Pacheco, Jun Nathan Santos
Date Created: 2022-08-15
Date Modified: 2025-04-20
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instruction:
    - Create a user-defined function to push (add) an item in the stack; display a message if it is overflow
    - Create a user-defined function to pop (delete) an item in the stack; display a message if it is underflow.
    - Validate the user input.

'''

def push_item(s):
    if len(s) == 5:
        print("Stack Overflow")
    else:
        item = input("Input item : ")
        s.append(item)
        top_item = s[len(s) - 1]
        top_index = len(s) - 1
        print("\nTop item:",top_item)
        print("Top index:",top_index)
        print("Stack items:")
        index = len(s)
        for i in range(index):
            index -= 1
            print(s[index])
    return s

def pop_item(s):
    if len(s) == 0:
        print("Stack Underflow")
    else:
        item_removed = s.pop()
        if len(s) != 0:
            top_index = len(s) - 1
        elif len(s) == 0:
            top_index = "None"
        print("\nItem removed:",item_removed)
        print("Top index:",top_index)
        print("Stack items:")
        if len(s) != 0:
            index = len(s)
            for i in range(index):
                index -= 1
                print(s[index])
        elif len(s) == 0:
            print("None")
    return s
    
def menu():
    stack = []
    choice = 1
    try:
        while choice != 3:
            print('''\nMenu:
    [1] Push
    [2] Pop
    [3] Exit''')
            choice = int(input("\nInput choice : "))
            if choice == 1:
                stack = push_item(stack)
            elif choice == 2:
                stack = pop_item(stack)
            elif choice != 3:
                print("Invalid choice. Try again.")
                menu()
    except ValueError:
        print("Invalid input. Try again.")
        menu()

#main
menu()

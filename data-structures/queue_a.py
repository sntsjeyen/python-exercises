'''

File Name: queue_a.py
Authors: Aljon James Pacheco, Jun Nathan Santos
Date Created: 2022-08-19
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that would show the queue operations and ask the user to input an item.
    - Set the limit to 5 and validate the user input for option.
    - Display the front item, front index, rear item, and rear index.
    - Display the items of the queues

'''

import array as arr

def enqueue_item(q, f_index, r_index):
    if len(q) == 5:
        print("The queue has reached its max limit.")
    else:
        item = int(input("\nInput item to add in the queue : "))
        q.append(item)
        print("Front item :",q[0])
        print("Front index :",f_index)
        print("Rear item :",q[-1])
        r_index += 1
        print("Rear index :",r_index)
        print("Queues :", end = " ")
        for i in q:
            print(i, end = " ")
        print()
    return q, r_index

def dequeue_item(q, f_index, r_index):
    if len(q) == 0:
        print("The queue is empty.")
    else:
        print("\nFirst item in the queue to be removed :",q[0])
        q.pop(0)
        if len(q) == 0:
            print("The queue is now empty.")
        else:
            print("Front item :",q[0])
            f_index += 1
            print("Front index :",f_index)
            print("Rear item :",q[-1])
            print("Rear index :",r_index)
            print("Queues :", end = " ")
            for i in q:
                print(i, end = " ")
            print()
    return q, f_index

def queue_options(queue, front_index, rear_index):
    choice = 1
    try:
        while choice != 3:
            print('''\nQueue Options:
    [1] Enqueue
    [2] Dequeue
    [3] Exit''')
            choice = int(input("\nInput choice : "))
            try:
                if choice == 1:
                    queue, rear_index = enqueue_item(queue, front_index, rear_index)
                elif choice == 2:
                    queue, front_index = dequeue_item(queue, front_index, rear_index)
                elif choice == 3:
                    print("Program exited.")
                    exit()
                else:
                    print("Invalid choice. Try again.")
                    queue, front_index, rear_index = queue_options(queue, front_index, rear_index)
            except TypeError:
                queue, front_index, rear_index = queue_options(queue, front_index, rear_index)
    except ValueError:
        print("Invalid input. Try again.")
        queue, front_index, rear_index = queue_options(queue, front_index, rear_index)
    return queue, front_index, rear_index

if __name__ == '__main__':
    queue = arr.array('i', [])
    front_index = 0
    rear_index = -1
    queue, front_index, rear_index = queue_options(queue, front_index, rear_index)

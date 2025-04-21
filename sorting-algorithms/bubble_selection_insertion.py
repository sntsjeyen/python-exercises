'''

File Name: bubble_selection_insertion.py
Authors: Aljon James Pacheco, Jun Nathan Santos
Date Created: 2022-09-28
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that accepts an input of 6 distinct numbers.
    - Display the output based on the selected sorting process and order of elements.
    - Validate user input
    - Create a menu that includes bubble, selection, and insertion sorting processes.
    - Sort either in ascending or descending order.

'''

# The function that displays the bubble sorting process and the ordered elements is defined.
def bubble_sort(num_arr):
    print('\nSort elements in:\n  [1] Ascending Order\n  [2] Descending Order')
    order_choice = int(input('\nEnter option : '))
    if (order_choice != 1) and (order_choice != 2):
        print('Invalid option. Try again.')
        return
    else:
        sort_arr = []
        for n in num_arr:
            sort_arr.append(n)
        length = len(sort_arr)
        print('\nUnsorted :',* sort_arr)
        for i in range(length):
            print('\nLoop ' + str(i))
            for j in range(length - 1):
                if order_choice == 1:
                    if sort_arr[j] > sort_arr[j + 1]:
                        sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
                elif order_choice == 2:
                    if sort_arr[j] < sort_arr[j + 1]:
                        sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
                print(sort_arr)

# The function that displays the selection sorting process and the ordered elements is defined.
def selection_sort(num_arr):
    print('\nSort elements in:\n  [1] Ascending Order\n  [2] Descending Order')
    order_choice = int(input('\nEnter option : '))
    if (order_choice != 1) and (order_choice != 2):
        print('Invalid option. Try again.')
        return
    else:
        sort_arr = []
        for n in num_arr:
            sort_arr.append(n)
        length = len(sort_arr)
        print('\nUnsorted :',* sort_arr)
        for i in range(length):
            print('\nLoop ' + str(i))
            min_ind = i
            for j in range(i + 1, length):
                if order_choice == 1:
                    if sort_arr[j] < sort_arr[min_ind]:
                        min_ind = j
                elif order_choice == 2:
                    if sort_arr[j] > sort_arr[min_ind]:
                        min_ind = j
            sort_arr[i], sort_arr[min_ind] = sort_arr[min_ind], sort_arr[i]
            print(sort_arr)

# The function that displays the insertion sorting process and the ordered elements is defined.
def insertion_sort(num_arr):
    print('\nSort elements in:\n  [1] Ascending Order\n  [2] Descending Order')
    order_choice = int(input('\nEnter option : '))
    if (order_choice != 1) and (order_choice != 2):
        print('Invalid option. Try again.')
        return
    else:
        sort_arr = []
        for n in num_arr:
            sort_arr.append(n)
        length = len(sort_arr)
        print('\nUnsorted :',* sort_arr)
        for i in range(1, length):
            print('\nLoop ' + str(i))
            if order_choice == 1:
                while (sort_arr[i] < sort_arr[i - 1]) and (i > 0):
                    sort_arr[i], sort_arr[i - 1] = sort_arr[i - 1], sort_arr[i]
                    i -= 1
                    print(sort_arr)
            if order_choice == 2:
                while (sort_arr[i] > sort_arr[i - 1]) and (i > 0):
                    sort_arr[i], sort_arr[i - 1] = sort_arr[i - 1], sort_arr[i]
                    i -= 1
                    print(sort_arr)
            print(sort_arr)

# The function that lets the user input 6 distinct numbers is defined.
def input_numbers(count, num_arr):
    while len(num_arr) < 6:
        try:
            num = int(input('Enter number ' + str(count) + ' : '))
            if num in num_arr:
                print('>> The number already exists.')
            else:
                num_arr.append(num)
                count += 1
        except:
            print('>> Invalid input. Enter an integer.')
            count = len(num_arr) + 1
            input_numbers(count, num_arr)

# The function that displays the sorting options and lets the user choose among them is defined.
def sorting_options(num_arr):
    process_choice = 1
    try:
        while process_choice != 4:
            print('\nSorting Process:\n  [1] Bubble Sort\n  [2] Selection Sort\n  [3] Insertion Sort\n  [4} Exit')
            process_choice = int(input('\nEnter option : '))
            if process_choice == 1:
                bubble_sort(num_arr)
            elif process_choice == 2:
                selection_sort(num_arr)
            elif process_choice == 3:
                insertion_sort(num_arr)
            elif process_choice != 4:
                print('Invalid option. Try again.')
    except:
        print('Invalid input. Try again.')
        sorting_options(num_arr)

if __name__ == '__main__':
    num_arr = []
    print('\nInput 6 distinct numbers.')
    count = 1
    input_numbers(count, num_arr)
    sorting_options(num_arr)
'''

File Name: tuple_a.py
Authors: Angel May Maniago, Jun Nathan Santos, John Florence Singson
Date Created: 2022-04-17
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instruction:
    - Write a program that would input values in a tuple and perform tuple operations (built-in methods/functions).

'''

try:
    # The program displays the elements of the tuple.
    def display_tuple(t):
        print('\nTuple contains : ',end='')
        l = (len(t)) - 1
        for e in t:
            if e != t[l]:
                print(e,end=', ')
            if e == t[l]:
                print(e)

    # User inputs starting and ending values that the program will use as index in tuple slicing.
    def tuple_slicing(t):
        print('\nSlicing in tuples:')
        s = int(input('  Enter starting value : '))
        e = int(input('  Enter ending value   : '))
        l = e - 1
        print('  Elements : ',end='')
        for e in t[s:e]:
            if e != t[l]:
                print(e,end=', ')
            if e == t[l]:
                print(e)

    # The program displays the length of the tuple.
    def display_length(t):
        print('\nDisplay the length of a tuple')
        length = len(t)
        print('  Length :',length)

    # User inputs a number and the program will display the element having that inputted number as index.
    def display_element(t):
        print('\nDisplay element:')
        num = int(input('  Enter negative number : '))
        element = t[num]
        print('  Element : ',element)

    # User inputs an element and the program will display the count of that element in the tuple.
    def count_element(t):
        print('\nCount in tuple')
        element = input('  Enter an element : ')
        cnt = t.count(element)
        print('  Count :',cnt)

    # User inputs an index (number) and the program will display which element has that index.
    def display_index(t):
        print('\nDisplay index:')
        element = input('  Enter element : ')
        ind = t.index(element)
        print('  Index :',ind)

    # User inputs an element and the program will check if that element is in the tuple. 
    def check_element(t):
        print('\nElement in tuple:')
        val = input('  Input value : ')
        if val in t:
            print('  Output : True')
        else:
            print('  Output : False')

    # The program displays the element with the highest value.
    def display_max(t):
        print('\nMaximum')
        print('  Output :',max(t))

    # The program displays the element with the lowest value.
    def display_min(t):
        print('\nMinimum')
        print('  Output :',min(t))
        print()

    # main
    my_tuple = ('l', 'h', 'a', 'me', 's', 'i', 'w', 'r', 'l', 'j')
    display_tuple(my_tuple)
    tuple_slicing(my_tuple)
    display_length(my_tuple)
    display_element(my_tuple)
    count_element(my_tuple)
    display_index(my_tuple)
    check_element(my_tuple)
    display_max(my_tuple)
    display_min(my_tuple)

except:
    print('Invalid input. Try again.')
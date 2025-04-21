'''

File Name: merge_sort.py
Authors: Aljon James Pacheco, Jun Nathan Santos
Date Created: 2022-10-24
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that accepts an input of 8 distinct numbers.
    - Apply the process of the merge sort algorithm.
    - Display the output either in ascending or descending order..

'''

def displayOutput(sortedList, order):
    if order == 'a':
        print('\nSorted Values in Ascending Order:')
    elif order == 'b':
        print('\nSorted Values in Descending Order:')
    print(* sortedList)

def mergeSort(sortedList, order):
    print('Divided :', sortedList)
    if len(sortedList) > 1:
        mid = len(sortedList) // 2
        leftList = sortedList[:mid]
        rightList = sortedList[mid:]

        #print('Divided  :', leftList)
        mergeSort(leftList, order)
        #print('Divided  :', rightList)
        mergeSort(rightList, order)

        i = j = k = 0
        while i < len(leftList) and j < len(rightList):
            if order == 'a':
                if leftList[i] < rightList[j]:
                    sortedList[k] = leftList[i]
                    i += 1
                else:
                    sortedList[k] = rightList[j]
                    j += 1
                k += 1
            elif order == 'b':
                if leftList[i] > rightList[j]:
                    sortedList[k] = leftList[i]
                    i += 1
                else:
                    sortedList[k] = rightList[j]
                    j += 1
                k += 1

        while i < len(leftList):
            sortedList[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            sortedList[k] = rightList[j]
            j += 1
            k += 1

    print('Merged  :', sortedList)

def chooseOrder(numList):
    print('\nOrder:\n  [a] Ascending\n  [b] Descending\n  [c] Exit/Close')
    order = input('\nEnter order choice: ').lower()
    while order != 'c':
        if order == 'a' or order == 'b':
            sortedList = []
            for n in numList:
                sortedList.append(n)
            print('Given values :', numList)
            mergeSort(sortedList, order)
            displayOutput(sortedList, order)
            print('\nOrder:\n  [a] Ascending\n  [b] Descending\n  [c] Exit/Close')
            order = input('\nEnter order choice: ').lower()
        else:
            print('>> Invalid choice. Try again')
            order = input('\nEnter order choice: ').lower()

def inputNum(numList):
    try:
        while len(numList) < 8:
            num = int(input('Number ' + str(len(numList) + 1) + ' : '))
            if num in numList:
                print('>> Number already in list. Input another number.')
            else:
                numList.append(num)
    except:
        print('>> Invalid input. Try again.')
        inputNum(numList)

if __name__ == '__main__':
    numList = []
    print('Input 8 numbers.')
    inputNum(numList)
    chooseOrder(numList)
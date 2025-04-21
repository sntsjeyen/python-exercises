'''

File Name: shell_sort.py
Author: Jun Nathan Santos
Date Created: 2022-10-17
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that would display the output using shell sorting algorithm in descending order.
    - Use these values: 25, 63, 45, 78, 30, 96, 15, 60

'''

def displayOutput(numList, sortedList):
    print('Algorithm : Shell Sort\nOrder: Descending')
    print('\nGiven elements: ')
    print(* numList)
    print('\nSorted elements: ')
    print(* sortedList)

def insertionSort(sortedList, size):
    for i in range(1, size):
        while (sortedList[i] > sortedList[i - 1]) and (i > 0):
            sortedList[i], sortedList[i - 1] = sortedList[i - 1], sortedList[i]
            i -= 1

def shellSort(sortedList, size):
    interval = 4
    for i in range(interval, size):
        temp = sortedList[i]
        j = i
        while j >= interval and sortedList[j - interval] < temp:
            sortedList[j] = sortedList[j - interval]
            j -= interval

        sortedList[j] = temp
    insertionSort(sortedList, size)

if __name__ == '__main__':
    numList = [25, 63, 45, 78, 30, 96, 15, 60]
    sortedList = []
    for n in numList:
        sortedList.append(n)
    size = len(sortedList)
    shellSort(sortedList, size)
    displayOutput(numList, sortedList)
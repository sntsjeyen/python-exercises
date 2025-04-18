'''

File Name: list_b.py
Author: Jun Nathan Santos
Date Created: 2022-03-31
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

'''

# Reads a student's test results and computes the average with the lowest score discarded

try:
    enter_score = 'Y'
    test_scores = []
    print()

    while (enter_score == 'Y'):
        score = float(input('Enter student score : '))
        test_scores.append(score)
        enter_score = input('Do you want to enter another score? Answer [Y/N] : ').upper()

    test_scores.sort(); test_scores.reverse(); 
    print('\nList of scores in descending order :', test_scores)

    sum = 0
    for s in test_scores:
        sum += s
    print('\nSum of all the scores :', sum)

    min_value = min(test_scores)
    sum -= min_value
    print('Sum of all the scores minus the minimum value :', sum)

    average = sum / (len(test_scores)-1)
    print('Average of all the scores minus the minimum value : {0:.2f}'.format(average))

except:
    print('Invalid input. Try again.')
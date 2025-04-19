'''

File Name: dictionary_b.py
Authors: Aljon James Pacheco, Jun Nathan Santos
Date Created: 2022-08-01
Date Modified: 2025-04-19
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instruction:
    - Write a program that accepts an input of 3 records of students using a dictionary.
    - Compute the average of the quiz and assignment.
    - Save to a text file.

'''

# Accepts name input
def enter_name():
    name = input('\nEnter name : ')
    return name

# Accepts quiz score input
def enter_quiz():
    quiz_sum = 0
    for x in range(3):
        quiz = int(input('Enter quiz {} score : '.format(x + 1)))
        quiz_sum += quiz
        quiz_ave = quiz_sum / 3
        quiz_ave = round(quiz_ave, 2)
    return quiz_ave

# Accepts assignment score input
def enter_assign():
    assign_sum = 0
    for x in range(2):
        assign = int(input('Enter assignment {} score : '.format(x + 1)))
        assign_sum += assign
        assign_ave = assign_sum / 2
        assign_ave = round(assign_ave, 2)
    return assign_ave

# Accepts exam score input
def enter_exam():
    exam = int(input('Enter exam score : '))
    return exam

if __name__ == '__main__':
    print('Enter three (3) quiz scores and two (2) assignment scores for each student.')

    F1 = {'Name': enter_name(), 'AveQuiz': enter_quiz(), 'AveAssign': enter_assign(), 'Exam': enter_exam()}
    F2 = {'Name': enter_name(), 'AveQuiz': enter_quiz(), 'AveAssign': enter_assign(), 'Exam': enter_exam()}
    F3 = {'Name': enter_name(), 'AveQuiz': enter_quiz(), 'AveAssign': enter_assign(), 'Exam': enter_exam()}

    record = {'RF1': F1, 'RF2': F2, 'RF3': F3}

    text = open('record.txt', 'w+')
    text.write(f'Name\t\tAveQuiz\t\tAveAssign\tExam\n')
    for x in record:
        text.write(f'{record[x]['Name']}\t\t{record[x]['AveQuiz']}\t\t{record[x]['AveAssign']}\t\t{record[x]['Exam']}')
        text.write('\n')

    text.close()
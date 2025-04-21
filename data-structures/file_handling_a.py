'''

File Name: file_handling_a.py
Author: Jun Nathan Santos
Date Created: 2022-08-01
Date Modified: 2025-04-19
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instruction:
    - Write a python program that would read the data from

'''

def read_name(txt):
    name = txt.readline()
    return name

def read_quiz(txt):
    txt.readline()
    quiz1 = int(txt.readline())
    quiz2 = int(txt.readline())
    quiz3 = int(txt.readline())
    quiz4 = int(txt.readline())
    return quiz1, quiz2, quiz3, quiz4

def read_assign(txt):
    txt.readline()
    assign1 = int(txt.readline())
    assign2 = int(txt.readline())
    return assign1, assign2

def read_exam(txt):
    txt.readline()
    exam = int(txt.readline())
    return exam

def compute_quiz_ave(quiz1, quiz2, quiz3, quiz4):
    quiz_ave = (quiz1 + quiz2 + quiz3 + quiz4) / 4
    quiz_ave = round(quiz_ave, 2)
    return quiz_ave

def compute_assign_ave(assign1, assign2):
    assign_ave = (assign1 + assign2) / 2
    return assign_ave

def compute_grade(quiz_ave, assign_ave, exam):
    grade = (quiz_ave + assign_ave + exam) / 3
    grade = round(grade, 2)
    return grade

def decide_remarks(grade):
    if grade >= 75:
        remarks = 'Passed'
    else:
        remarks = 'Failed'
    return remarks

def display_output(name, quiz_ave, assign_ave, exam, grade, remarks):
    new_text = open('output.txt', 'w+')
    new_text.write('Name : ' + name)
    new_text.write('Average (Quiz) : ' + str(quiz_ave) + '\n')
    new_text.write('Average (Assignment) : ' + str(assign_ave) + '\n')
    new_text.write('Exam : ' + str(exam) + '\n')
    new_text.write('Grade : ' + str(grade) + '\n')
    new_text.write('Remarks : ' + remarks)
    new_text.close()

if __name__ == '__main__':
    # Move records.txt file from text-files to C drive or modify file path
    text_file = open('C:\\records.txt', 'r')
    n = read_name(text_file)
    q1, q2, q3, q4 = read_quiz(text_file)
    a1, a2 = read_assign(text_file)
    e = read_exam(text_file)
    text_file.close()

    qa = compute_quiz_ave(q1, q2, q3, q4)
    aa = compute_assign_ave(a1, a2)
    g = compute_grade(qa, aa, e)
    r = decide_remarks(g)
    display_output(n, qa, aa, e, g, r)
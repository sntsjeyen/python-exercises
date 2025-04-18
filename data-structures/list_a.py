'''

File Name: list_a.py
Author: Jun Nathan Santos
Date Created: 2022-03-31
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

'''

# Accepts the hours worked by each employee and then show the total gross pay for all workers with an hourly rate of Php 675.75

try:
    employee = 0
    hours_worked = []

    for h in range(7):
        employee += 1
        hours = float(input('Enter hours worked for employee ' + str(employee) + ' >> '))
        hours_worked.append(hours)

    print('\nList of hours worked :', hours_worked, '\n')
    print('*'*20, '\n')
    employee = 0

    for h in hours_worked:
        employee += 1
        gross_pay = h * 675.75
        print('Gross pay for employee ' + str(employee) + ': {0:,.2f}'.format(gross_pay))

except:
    print('Invalid input. Try again.')
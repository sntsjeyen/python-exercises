'''

File Name: tuition_calculator.py
Author: Jun Nathan Santos
Date Created: 2022-01-30
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a program that computes a tuition based on corresponding conditions.
    - User must input name, year level, course code, total number of units, and number of labs
    - The program should display a breakdown of fees.
    - Tuition must be equal to the product of the total number of units and the rate per unit.
    - Miscellaneous fee is computed as 6.7% of tuition.
    - Use if, if-else, if-elif, or nested if-else statements.

'''

try:
    # Student name
    print('Hello! This tuition calculator computes your tuition fee. Kindly provide the required information:')
    name = input('\nStudent Name      >>  ')

    # Year level
    print('''
    Year Level  |  Rate Per Unit
    ————————————————————————————
    1           |  1,325.00
    2           |  1,240.00
    3           |  1,195.00
    4/5         |  1,085.00
    ''')
    year_level = 0
    while not (year_level >= 1 and year_level <= 5):
        year_level = int(input('Year Level        >>  '))
        if not (year_level >= 1 and year_level <= 5):
            print('Invalid year level. Enter a value from 1 to 5.')

    # Course code
    print('''
    Course Code  |  Course       |  Lab Rate
    ————————————————————————————————————————
    IT           |  IT           |  4,325.00
    N            |  Nursing      |  4,500.00
    E            |  Engineering  |  3,987.00
    C            |  Culinary     |  4,113.00
    Others       |  —            |  0.00
    ''')
    course_code = input('Course Code       >>  ')

    # Total number of units
    units = int(input('Number of Units   >>  '))

    # Number of labs
    labs = int(input('Number of Labs    >>  '))

    # Terms of payment
    print('''
    Terms of Payment  |  Discount
    —————————————————————————————
    1                 |  2,000.00
    2                 |  1,000.00
    Monthly           |  0.00
    ''')
    payment_terms = int(input('Terms of Payment  >>  '))

    # Computation for tuition fee
    if year_level == 1:
        tuition_fee = units * 1325
    elif year_level == 2:
        tuition_fee = units * 1240
    elif year_level == 3:
        tuition_fee = units * 1195
    elif year_level == 4 or 5:
        tuition_fee = units * 1085

    # Computation for lab fee
    if course_code == 'IT' or 'it':
        lab_fee = labs * 4325
    elif course_code == 'N' or 'n':
        lab_fee = labs * 4500
    elif course_code == 'E' or 'e':
        lab_fee = labs * 3987
    elif course_code == 'C' or 'c':
        lab_fee = labs * 4113
    else:
        lab_fee = labs * 0

    # Computation for miscellaneous fee and total amount
    misc_fee = tuition_fee * 0.067
    total_amount = tuition_fee + lab_fee + misc_fee

    # Computation for balance
    if payment_terms == 1:
        discount = 2000
        initial_payment = total_amount - discount
        balance = 0
    elif payment_terms == 2:
        discount = 1000
        initial_payment = (total_amount - discount) / 2
        balance = initial_payment
    elif payment_terms == 3:
        discount = 0
        initial_payment = total_amount / 10
        balance = total_amount - initial_payment

    # Breakdown of fees
    print('\nBREAKDOWN OF FEES')
    print('Tuition Fee                   :  Php {0:,.2f}'.format(tuition_fee))
    print('Laboratory Fee                :  Php {0:,.2f}'.format(lab_fee))
    print('Miscellaneous Fee             :  Php {0:,.2f}'.format(misc_fee))
    print('Total Amount Due              :  Php {0:,.2f}'.format(total_amount))
    print('Discount                      :  Php {0:,.2f}'.format(discount))
    print('Initial Payment               :  Php {0:,.2f}'.format(initial_payment))
    print('Balance After Inital Payment  :  Php {0:,.2f}'.format(balance))

except:
    print('There has been an error. Try again.')
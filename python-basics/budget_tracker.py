'''

File Name: budget_tracker.py
Author: Jun Nathan Santos
Date Created: 2022-02-24
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a program that lets the user input a certain amount and item amounts until cash has been maximized.
    - If the amount of the last item exceeds the certain amount inputted, it shall not be added to the total amount.
    - The program shall compute for and display the tax (12% of the total expenses), total expenses, and the change.
    - Only use repetition structures, decision structures, and exception handling.

'''

try:
    # Enter certain amount
    amount = float(input('Enter amount : Php '))
    balance = amount

    # Enter expenses
    print('\nEnter your expenses:')
    total_expenses = 0
    n = 0
    new_item = True
    
    while new_item == True:
        n += 1
        expense = float(input('Item ' + str(n) + '\t :  Php '))
        total_expenses += expense
        balance -= expense
        new_item = expense < balance
        if expense > balance:
            total_expenses -= expense
            print('Last item cannot be added. Insufficient cash.\n')
            tax = total_expenses * 0.12
            change = amount - total_expenses

    # Display tax, total amount of expenses, and change
    print('Your total tax       :  Php {0:.2f}'.format(tax))
    print('Your total expenses  :  Php {0:.2f}'.format(total_expenses))
    print('Your change          :  Php {0:.2f}'.format(change))

except:
    print('There has been an error. Try again.') 
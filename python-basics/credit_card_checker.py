'''

File Name: credit_card_checker.py
Author: Jun Nathan Santos
Date Created: 2022-03-17
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a program that inputs the currently available balance of a credit card and the total amount of the new purchases.
    - Compute for the total amount of payment which includes 8% interest of the new purchases.
    - Compute also for the new remaining balance of the credit card.
    - If the total amount of payment is greater than the available balance, it displays a message notifying user that purchase is not allowed.
    - Write the following functions in the program:
        + pasok(). Accepts from the user the credit card available balance and amount of new purchase and returns both.
        + c_interest(). Should accept amount of new purchase as argument and return the corresponding interest.
        + c_total(). Should accept amount of new purchase and interest as arguments and return the total amount of payment.
        + c_balance(). Should accept current available balance and total amount of payment as arguments and return the new remaining balance or the appropriate notification.

'''

try:
    # Asks user for balance and new purchase inputs and returns both
    def pasok():
        balance = float(input('\nEnter credit card available balance : Php '))
        new_purchase = float(input('Enter amount of new purchase : Php '))
        return balance, new_purchase

    # Computes interest using new purchase value
    def c_interest(new_purchase):
        interest = new_purchase * 0.08
        return interest

    # Computes total amount of payment
    def c_total(new_purchase, interest):
        total = new_purchase + interest
        return total

    # Computes new balance
    def c_balance(balance, total):  
        new_balance = balance - total
        return new_balance

    if __name__ == '__main__':
        # Function calls
        balance, new_purchase = pasok()
        interest = c_interest(new_purchase)
        total = c_total(new_purchase, interest)
        new_balance = c_balance(balance, total)

        # Displaying output
        print('\nSUMMARY')
        print('Credit card current available balance : Php {0:,.2f}'.format(balance))
        print('Amount of new purchase : Php {0:,.2f}'.format(new_purchase))
        print('Interest of new purchase : Php {0:,.2f}'.format(interest))
        print('Total amount of payment : Php {0:,.2f}'.format(total))
        print('Remaining balance of credit card : Php {0:,.2f}'.format(new_balance))

except:
    print('There has been an error. Try again.')
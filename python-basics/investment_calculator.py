'''

File Name: investment_calculator.py
Author: Jun Nathan Santos
Date Created: 2022-02-21
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Make an investment calculator based on the following:
        + Initial investment: Amount of available money for initial investment
        + Annual investment: Amount that you plan to add every year
        + Annual interest rate (%): The percentage rate at which the investment grows each year
        + Number of years of investment: Length of time of the investment
    - Initial investment, annual investment, and annual interest rate should be greater than 0.
    - Calculator will compute for the following:
        + Interest earned annually
        + Total savings at the end of each year
        + Total incurred investment

'''

try:
    # User inputs
    initial_inv = float(input('Enter initial investment        :  Php '))
    annual_inv = float(input('Enter annual investment         :  Php '))
    annual_interest_rate = float(input('Enter annual interest rate (%)  :  '))
    years = int(input('Enter number of years           :  '))

    # Output header
    print('\nYear\t\tAnnual Investment\tSavings')

    # Setting values
    annual_interest_rate /= 100
    savings = 0

    # Loop for calculation and output
    for y in range(0, years):
        if savings == 0:
            total_inv = initial_inv + annual_inv
            annual_interest = initial_inv * annual_interest_rate
            savings = total_inv + annual_interest
            y += 1
        else:
            annual_interest = savings * annual_interest_rate
            savings += annual_inv
            savings += annual_interest
            y += 1
        print(y, '\t\tPhp {0:,.2f}'.format(annual_interest), '\t\tPhp {0:,.2f}'.format(savings))

    # Display total incurred investment
    print('\nAt the end of', years, 'years, your savings is Php {0:,.2f}'.format(savings))
    
except:
    print('There has been an error. Try again.')
'''

File Name: shipping_estimator.py
Author: Jun Nathan Santos
Date Created: 2022-02-24
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a program with data fields for the weight (oz), shipping method, and shipping cost.
    - The shipping method is a character: 'A' for Air, 'T' for Truck, or 'M' for Mail.
    - The shipping cost is based on a provided table.
    - The program totals the shipping cost and runs repeatedly.
    
'''

try:
    # Set initial values
    repeat_again = 'Y'
    total_cost = 0

    # Loop for shipping cost estimation
    while (repeat_again == 'Y') or (repeat_again == 'y'):
        # Display shipping cost estimation details
        print('''Here are the details you need to know for the shipping cost:
        Weight       |  Air (A)     |  Truck (T)   |  Mail (M)
        ————————————————————————————————————————————————————————
        1 to 8.99    |  Php 102.00  |  Php 76.89   |  Php 25.63
        9 to 16.99   |  Php 153.78  |  Php 120.46  |  Php 76.89
        17 and over  |  Php 230.76  |  Php 166.60  |  Php 120.46
        ''')

        # Input values
        weight = float(input('Enter weight (oz)              >>  '))
        method = input('Enter shipping method [A/T/M]  >>  ')

        # Calculate total shipping cost
        if (method == 'A') or (method == 'a'):
            shipping_method = 'Air'
            if weight >= 1 and weight <= 8.99:
                shipping_cost = 102
            elif weight >= 9 and weight <= 16.99:
                shipping_cost = 153.78
            elif weight >= 17:
                shipping_cost = 230.76
        elif (method == 'T') or (method == 't'):
            shipping_method = 'Truck'
            if weight >= 1 and weight <= 8.99:
                shipping_cost = 76.89
            elif weight >= 9 and weight <= 16.99:
                shipping_cost = 120.46
            elif weight >= 17:
                shipping_cost = 166.60
        elif (method == 'M') or (method == 'm'):
            shipping_method = 'Mail'
            if weight >= 1 and weight <= 8.99:
                shipping_cost = 25.63
            elif weight >= 9 and weight <= 16.99:
                shipping_cost = 76.89
            elif weight >= 17:
                shipping_cost = 120.46
        total_cost += shipping_cost

        # Display shipping cost details
        print('Shipping Weight  :  {0:.2f}'.format(weight))
        print('Shipping Method  : ', shipping_method)
        print('Shipping Cost    :  Php {0:.2f}'.format(shipping_cost))
        print('Total Cost       :  Php {0:.2f}'.format(total_cost))

        # Prompt for user to estimate again
        repeat_again = input('\nDo you want to estimate shipping cost again? [Enter Y to continue]  >>  ')

except:
    print('There has been an error. Try again.') 
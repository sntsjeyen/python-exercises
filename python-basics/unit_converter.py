'''

File Name: unit_converter.py
Author: Jun Nathan Santos
Date Created: 2022-03-17
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a module function program that converts the following:
        + Inch to centimeter and vice versa -> 1 inch = 2.54 cm
        + Kilogram to pound and vice versa -> 1 kg = 2.205 lb
        + Meter to feet and vice versa -> 1 meter = 3.2808 feet
    - Make a menu-driven python program that calls the module function program containing six value-returning functions.

'''

import unit_converter_utils as conversion

try:
    # Function for displaying menu
    def menu():
        print('''\nConversion Menu
        [1]  Inch to Centimeter
        [2]  Centimeter to Inch
        [3]  Kilogram to Pound
        [4]  Pound to Kilogram
        [5]  Meter to Feet
        [6]  Feet to Meter
        [7]  Exit
        ''')

    if __name__ == '__main__':
        choice = 0

        # Loop for process
        while choice != 7:
            menu()
            choice = int(input('Enter choice : '))

            if choice == 1:
                inch = float(input('\nEnter length of inch to convert to centimeter : '))
                print('Equivalent centimeter : {0:.2f}'.format(conversion.in_cm(inch)))
            elif choice == 2:
                centimeter = float(input('\nEnter length of centimeter to convert to inch : '))
                print('Equivalent inch : {0:.2f}'.format(conversion.cm_in(centimeter)))
            elif choice == 3:
                kilogram = float(input('\nEnter weight in kilogram to convert to pound : '))
                print('Equivalent pound : {0:.2f}'.format(conversion.kg_lb(kilogram)))
            elif choice == 4:
                pound = float(input('\nEnter weight in pound to convert to kilogram : '))
                print('Equivalent kilogram : {0:.2f}'.format(conversion.lb_kg(pound)))
            elif choice == 5:
                meter = float(input('\nEnter length in meter to convert to feet : '))
                print('Equivalent feet : {0:.2f}'.format(conversion.m_ft(meter)))
            elif choice == 6:
                feet = float(input('\nEnter length in feet to convert to meter : '))
                print('Equivalent meter : {0:.2f}'.format(conversion.ft_m(feet)))
            elif choice == 7:
                print('Program terminated.')
                break
            else:
                print('Invalid choice. Try again.')

except:
    print('There has been an error. Try again.') 
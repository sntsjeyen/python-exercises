'''

File Name: taxi_fare_calculator.py
Author: Jun Nathan Santos
Date Created: 2022-01-30
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a program that computes for the taxi fare based on given conditions.
    - The flag down rate is Php 60; a rate of Php 4.50 is added for each kilometer or every after 2 minutes.
    - The total fare will be whichever is higher; amount is only increased for each full kilometer or after every 2 minutes.
    - Ask the user to input the distance traveled in kilometers and the duration of the ride in minutes.
    - Display the total fare.
    - Only use if, if-else, if-elif, or nested if-else statements.

'''

try:
    # Constant values
    RATE = 60
    ADDED_RATE = 4.50

    # Inputs for distance and duration
    distance = float(input('Distance Traveled (km)  >>  '))
    duration = float(input('Duration of Ride (min)  >>  '))

    # Computation for total fare based on distance
    total_added_rate_1 = distance * ADDED_RATE
    total_fare_1 = RATE + total_added_rate_1

    # Computation for total fare based on duration
    two_minute = duration // 2
    total_added_rate_2 = two_minute * ADDED_RATE
    total_fare_2 = RATE + total_added_rate_2

    # Choosing the higher total fare
    if total_fare_1 != total_fare_2:
        if total_fare_1 > total_fare_2:
            total_fare = total_fare_1
        elif total_fare_1 < total_fare_2:
            total_fare = total_fare_2
    else:
        total_fare = total_fare_1

    # Displaying the total fare
    print('\nTotal Fare: Php {0:,.2f}'.format(total_fare))

except:
    print('There has been an error. Try again.')
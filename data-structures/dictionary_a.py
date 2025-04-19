'''

File Name: dictionary_a.py
Author: Jun Nathan Santos
Date Created: 2022-04-28
Date Modified: 2025-04-19
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instruction:
    - Write a program that creates a dictionary containing course codes with their corresponding room numbers, instructors, and schedules.

'''

# The program defines the variable 'try_again' to proceed with the looping.
try_again = 'Y'

# The program contains a looping structure to let the user try again.
while try_again == 'Y':

    # The program creates dictionaries that contain course codes as keys with their corresponding room numbers, instructors, and schedules as values.
    course_room = {'6COMPRO2L': 'SJH-608', '6HCI': 'SJH-609', '6NETFUN': 'SJH-610', '6DMS': 'SJH-605', '6CSEC': 'MGN-202', '6DRAW1': 'SJH-607'}
    course_instructor = {'6COMPRO2L': 'Arcely Napalit', '6HCI': 'Adrian Magcalas', '6NETFUN': 'Paul Calimoso', '6DMS': 'Ma. Louella Salenga', '6CSEC': 'Marlon Tayag', '6DRAW1': 'Kahil Makisig Yu'}
    course_time = {'6COMPRO2L': '10:15 a.m.', '6HCI': '7:00 a.m.', '6NETFUN': '3:40 p.m.', '6DMS': '1:30 p.m.', '6CSEC': '2:35 p.m.', '6DRAW1': '4:45 p.m.'}

    # The program asks the user to input course code that will serve as the key in getting values.
    course_code = input('\nEnter the course : ').upper()

    # The program gets the values for the room number, instructor, and meeting time that correspond to the given course (key).
    room_number = course_room.get(course_code, 'Invalid course code.')
    instructor_name = course_instructor.get(course_code, 'Invalid course code.')
    meeting_time = course_time.get(course_code, 'Invalid course code.')

    # The program displays the room number, instructor, and meeting time for the course.
    print('Room Number      :', room_number)
    print('Instructor Name  :', instructor_name)
    print('Meeting Time     :', meeting_time)

    # The program asks the user if they want to try again or not.
    try_again = input('\nDo you want to try again? [Y/N] : ').upper()
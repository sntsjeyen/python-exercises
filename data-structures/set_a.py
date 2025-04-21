'''

File Name: dictionary_a.py
Author: Jun Nathan Santos
Date Created: 2022-04-28
Date Modified: 2025-04-19
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instruction:
    - Write a program that unlocks a text file named word.txt and shows a list of all the unique words found in the it. Use sets and must also have a TRY AGAIN. 

'''

# The program defines the variable 'try_again' to proceed with the looping.
try_again = 'Y'

# The program contains a looping structure to let the user try again.
while try_again == 'Y':

    # The program opens the text file named 'word.txt', reads the first line, and declares an empty list named 'word_list'.
    # Move word.txt file from text-files to C drive or modify file path
    text_file = open('C:\\word.txt', 'r')
    word = text_file.readline()
    word_list = []

    #The program contains another looping structure to add words in lowercase that have been stripped to the list named 'word_list'.
    while word != '':

        # The program splits the string named 'word', which returns a list of words.
        words = word.split(' ')

        # The program contains a nested looping structure for returning the words in lowercase and having them stripped.
        for w in words:
            w = w.lower()
            w = w.replace('\n','')
            w = w.strip('\'')
            w = w.strip('"')
            w = w.replace('\'s','')
            w = w.rstrip('.')
            w = w.rstrip(';')
            w = w.rstrip(',')

            # The program decides to add the string named 'w' if it contains something rather than '' and if it is an alphabetic string.
            if (w != '') and (w.isalpha()):
                word_list.append(w)

        # The program reads the next line in the text file.
        word = text_file.readline()

    # The program closes the opened text file.
    text_file.close()

    # The programs converts the list named 'word_list' into a set to contain the unique words.
    unique_words = set(word_list)
    print()

    # The program contains another looping structure to count the occurrences of each unique word in the text file.
    for u in unique_words:
        cnt = word_list.count(u)
        print(u,cnt)

    # The program asks the user if they want to try again or not.
    try_again = input('\nDo you want to try again? [Y/N] : ').upper()
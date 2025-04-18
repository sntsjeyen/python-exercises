'''

File Name: string_counter.py
Author: Jun Nathan Santos
Date Created: 2022-03-03
Date Modified: 2025-04-18
Course: 6COMPRO2L - Computer Programming 2
Institution: Holy Angel University

Instructions:
    - Write a program that will ask the user to input a sentence.
    - The program shall display the total number of words, letters, and occurrences of vowels and consonants in the sentence.
    
'''

try:
    # Input a sentence
    sentence = input('Input a sentence      :  ').lower()

    # Counts the words
    word_list = sentence.split(' ')
    word_count = len(word_list)

    # Counts the letters
    letter_list = sentence.rstrip('.')
    letter_list = letter_list.replace(' ', '')
    letter_count = len(letter_list)

    # Sets initial values for vowels and consonants
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_occ = 0
    consonant_occ = 0

    # Counts vowel and consonant occurrences
    for l in letter_list:
        if l in vowels:
            vowel_occ += 1
        else:
            consonant_occ += 1

    # Displays the count
    print('Word Count            : ',word_count)
    print('Letter Count          : ',letter_count)
    print('Vowel Occurences      : ',vowel_occ)
    print('Consonant Occurences  : ',consonant_occ)

except:
    print('There has been an error. Try again.')
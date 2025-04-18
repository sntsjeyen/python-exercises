try:
    sentence = input("Input a sentence      :  ").lower()

    word_list = sentence.split(" ")
    word_count = len(word_list)

    letter_list = sentence.rstrip(".")
    letter_list = letter_list.replace(" ", "")
    letter_count = len(letter_list)

    vowels = ["a", "e", "i", "o", "u"]
    vowel_occ = 0
    consonant_occ = 0

    for l in letter_list:
        if l in vowels:
            vowel_occ += 1
        else:
            consonant_occ += 1

    print("Word Count            : ",word_count)
    print("Letter Count          : ",letter_count)
    print("Vowel Occurences      : ",vowel_occ)
    print("Consonant Occurences  : ",consonant_occ)
except:
    print("\nInvalid. Please try again.")
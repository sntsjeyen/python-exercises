'''

File Name: list_c.py
Author: Jun Nathan Santos
Date Created: 2022-08-31
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a looping program that would read 10 numbers from a text file and assign it in the list.
    - Compute for the sum of all odd numbers and average of all even numbers.
    - Display the output in the text file.

'''

# Open the text file containing the numbers.
# Move number.txt file from text-files to C drive or modify file path
text_file = open("C:\\number.txt", "r")

# Get the numbers from the text file and assign them to a list.
numbers = text_file.readlines()
num_list = []
for n in numbers:
    if "\n" in n:
        n.rstrip(" ")
    num = int(n)
    num_list.append(num)

# Close the text file.
text_file.close()

# Get the odd and even numbers and assign them to separate lists.
odd_list = []
even_list = []
for n in num_list:
    if n % 2 == 1:
        odd_list.append(n)
    if n % 2 == 0:
        even_list.append(n)
odd_list.sort()
even_list.sort()

# Convert the list of odd numbers to string.
odd_str = ""
for n in odd_list:
    n_str = str(n) + " "
    odd_str += n_str

# Convert the list of even numbers to string.
even_str = ""
for n in even_list:
    n_str = str(n) + " "
    even_str += n_str
    
# Compute for the sum of odd numbers.
odd_sum = 0
for n in odd_list:
    odd_sum += n

# Compute for the average of even numbers.
even_sum = 0
for n in even_list:
    even_sum += n
even_ave = even_sum / 5

# Use the open() function to be able to display the output in a text file.
text_file = open("output.txt", "w+")

# Display the output by using write() function.
text_file.write("Odd Numbers : " + odd_str)
text_file.write("\nSum : " + str(odd_sum))
text_file.write("\nEven Numbers : " + even_str)
text_file.write("\nAverage : " + str(even_ave))

# Close the text file.
text_file.close()
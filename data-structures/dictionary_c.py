'''

File Name: list_c.py
Author: Jun Nathan Santos
Date Created: 2022-08-31
Date Modified: 2025-04-21
Course: 6DSALGO - Data Structures and Algorithms
Institution: Holy Angel University

Instructions:
    - Write a program that would assign the following to a dictionary:
        + Code: 1212
        + Product: Cream
        + Amount: 125
        + Quantity: 10
    - Compute for the subtotal, discount, and total Amount. Discount computation is 10% of subtotal.
    - Display the output in a text file.

'''

# Assign the following to a dictionary, which is named "item".
item = {"Code": 1212,
        "Product": "Cream",
        "Amount": 125,
        "Quantity": 10}

# Get the values from the dictionary.
code = item["Code"]
product = item["Product"]
amount = item["Amount"]
quantity = item["Quantity"]

# Get the key names from the dictionary.
key_names = list(item.keys()) 

# Assign the value of 10% discount to the variable discount_rate.
discount_rate = 0.10

# Compute for the required values.
total = amount * quantity
discount = total * discount_rate
total_amount = total - discount

# Use the open() function to be able to display the output in a text file.
text_file = open("output.txt", "w+")

# Display the output by using write() function.
text_file.write(key_names[0] + " : " + str(code))
text_file.write("\n" + key_names[1] + " : " + product)
text_file.write("\n" + key_names[2] + " : PHP " + str(amount))
text_file.write("\n" + key_names[3] + " : " + str(quantity))
text_file.write("\n\nTotal : PHP " + str(total))
text_file.write("\nDiscount : PHP " + str(discount))
text_file.write("\nTotal Amount to be Paid : PHP " + str(total_amount))

# Close the text file.
text_file.close()
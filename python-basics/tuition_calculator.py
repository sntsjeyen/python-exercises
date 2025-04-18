name = input("Student Name      :  ")
year_level = int(input("Year Level (1–5)  :  "))
course_code = input("Course Code       :  ")
num_units = int(input("Number of Units   :  "))
num_labs = int(input("Number of Labs    :  "))
num_payment_terms = int(input("Terms of Payment  :  "))

print("==========================")

if year_level == 1:
    tuition_fee = num_units * 1325
elif year_level == 2:
    tuition_fee = num_units * 1240
elif year_level == 3:
    tuition_fee = num_units * 1195
elif year_level == 4 or 5:
    tuition_fee = num_units * 1085

if course_code == "IT" or "it":
    lab_fee = num_labs * 4325
elif course_code == "N" or "n":
    lab_fee = num_labs * 4500
elif course_code == "E" or "e":
    lab_fee = num_labs * 3987
elif course_code == "C" or "c":
    lab_fee = num_labs * 4113
else:
    lab_fee = num_labs * 0

misc_fee = tuition_fee * 0.067
total_amount = tuition_fee + lab_fee + misc_fee

if num_payment_terms == 1:
    discount = 2000
    initial_payment = total_amount - discount
    balance = 0
elif num_payment_terms == 2:
    discount = 1000
    initial_payment = (total_amount - discount) / 2
    balance = initial_payment
elif num_payment_terms == 3:
    discount = 0
    initial_payment = total_amount / 10
    balance = total_amount - initial_payment

print("BREAKDOWN OF FEES")
print("Tuition Fee                   :  Php {0:.2f}".format(tuition_fee))
print("Laboratory Fee                :  Php {0:.2f}".format(lab_fee))
print("Miscellaneous Fee             :  Php {0:.2f}".format(misc_fee))
print("Total Amount Due              :  Php {0:.2f}".format(total_amount))
print("Discount                      :  Php {0:.2f}".format(discount))
print("Initial Payment               :  Php {0:.2f}".format(initial_payment))
print("Balance After Inital Payment  :  Php {0:.2f}".format(balance))
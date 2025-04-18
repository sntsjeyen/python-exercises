try:
    amount = float(input("Enter amount : Php "))
    balance = amount
    print("Enter your expenses:")
    total_expenses = 0
    n = 0
    new_item = True
    
    while new_item == True:
        n += 1
        expense = float(input("Item " + str(n) + "\t :  Php "))
        total_expenses += expense
        balance -= expense
        new_item = expense < balance
        if expense > balance:
            total_expenses -= expense
            print("Last item cannot be added. Insufficient cash.")
            tax = total_expenses * 0.12
            change = amount - total_expenses

    print("Your total tax       :  Php {0:.2f}".format(tax))
    print("Your total expenses  :  Php {0:.2f}".format(total_expenses))
    print("Your change          :  Php {0:.2f}".format(change))
except:
    print("Invalid. Please try again.") 
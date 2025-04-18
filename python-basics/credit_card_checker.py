def pasok():
    balance = float(input("\nEnter credit card available balance : Php "))
    new_purchase = float(input("Enter amount of new purchase : Php "))
    return balance, new_purchase

def c_interest(new_purchase):
    interest = new_purchase * 0.08
    return interest

def c_total(new_purchase, interest):
    total = new_purchase + interest
    return total

def c_balance(balance, total):  
    new_balance = balance - total
    return new_balance

#main
bal, n_p = pasok()
i = c_interest(n_p)
t = c_total(n_p, i)
n_b = c_balance(bal, t)

print("\n******** SUMMARY ********")
print("Credit card current available balance : Php {0:.2f}".format(bal))
print("Amount of new purchase : Php {0:.2f}".format(n_p))
print("Interest of new purchase : Php {0:.2f}".format(i))
print("Total amount of payment : Php {0:.2f}".format(t))
print("Remaining balance of credit card : Php {0:.2f}".format(n_b))
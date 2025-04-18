# SANTOS, Jun Nathan
# ICT-101

initial_inv = float(input("Enter initial investment        :  Php "))
annual_inv = float(input("Enter annual investment         :  Php "))
annual_interest_rate = float(input("Enter annual interest rate (%)  :  "))
years = int(input("Enter number of years           :  "))

print("")
print("Year\t\tAnnual Investment\tSavings")

annual_interest_rate /= 100
savings = 0

for y in range(0, years):
    if savings == 0:
        total_inv = initial_inv + annual_inv
        annual_interest = initial_inv * annual_interest_rate
        savings = total_inv + annual_interest
        y += 1
    else:
        annual_interest = savings * annual_interest_rate
        savings += annual_inv
        savings += annual_interest
        y += 1
    print(y,"\t\tPhp {0:.2f}".format(annual_interest),"\t\tPhp {0:.2f}".format(savings))

print("")
print("At the end of",years,"years, your savings is Php {0:.2f}".format(savings))
import conversion

def menu():
    print("""
    Conversion Menu
    [1]  Inch to Centimeter
    [2]  Centimeter to Inch
    [3]  Kilogram to Pound
    [4]  Pound to Kilogram
    [5]  Meter to Feet
    [6]  Feet to Meter
    [7]  Exit
    """)

choice = 0
while choice != 7:
    menu()
    choice = int(input("Enter choice : "))

    if choice == 1:
        print("Menu 1")
        inch = float(input("Enter length of inch to convert to centimeter : "))
        print("Equivalent centimeter : {0:.2f}".format(conversion.in_cm(inch)))
    elif choice == 2:
        print("Menu 2")
        centimeter = float(input("Enter length of centimeter to convert to inch : "))
        print("Equivalent inch : {0:.2f}".format(conversion.cm_in(centimeter)))
    elif choice == 3:
        print("Menu 3")
        kilogram = float(input("Enter weight in kilogram to convert to pound : "))
        print("Equivalent pound : {0:.2f}".format(conversion.kg_lb(kilogram)))
    elif choice == 4:
        print("Menu 4")
        pound = float(input("Enter weight in pound to convert to kilogram : "))
        print("Equivalent kilogram : {0:.2f}".format(conversion.lb_kg(pound)))
    elif choice == 5:
        print("Menu 5")
        meter = float(input("Enter length in meter to convert to feet : "))
        print("Equivalent feet : {0:.2f}".format(conversion.m_ft(meter)))
    elif choice == 6:
        print("Menu 6")
        feet = float(input("Enter length in feet to convert to meter : "))
        print("Equivalent meter : {0:.2f}".format(conversion.ft_m(feet)))
    elif choice == 7:
        print("Program terminating . . . ")
        break
    else:
        print("Invalid choice. Try again.")
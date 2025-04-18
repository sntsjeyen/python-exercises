try:
    repeat_again = "Y"
    total_cost = 0
    while (repeat_again == "Y") or (repeat_again == "y"):
        print("\n******************************")
        weight = float(input("\nEnter weight (oz) : "))
        print("Shipping Method")
        print("\t[A] Air")
        print("\t[T] Truck")
        print("\t[M] Mail")

        method = input("\nEnter shipping method: ")

        if (method == "A") or (method == "a"):
            shipping_method = "Air"
            if weight >= 1 and weight <= 8.99:
                shipping_cost = 102
            elif weight >= 9 and weight <= 16.99:
                shipping_cost = 153.78
            elif weight >= 17:
                shipping_cost = 230.76
        elif (method == "T") or (method == "t"):
            shipping_method = "Truck"
            if weight >= 1 and weight <= 8.99:
                shipping_cost = 76.89
            elif weight >= 9 and weight <= 16.99:
                shipping_cost = 120.46
            elif weight >= 17:
                shipping_cost = 166.60
        elif (method == "M") or (method == "m"):
            shipping_method = "Mail"
            if weight >= 1 and weight <= 8.99:
                shipping_cost = 25.63
            elif weight >= 9 and weight <= 16.99:
                shipping_cost = 76.89
            elif weight >= 17:
                shipping_cost = 120.46

        total_cost += shipping_cost

        print("Shipping Weight  :  {0:.2f}".format(weight))
        print("Shipping Method  : ",shipping_method)
        print("Shipping Cost    :  Php {0:.2f}".format(shipping_cost))
        print("Total Cost       :  Php {0:.2f}".format(total_cost))
        print("\n******************************")
        repeat_again = input("\nDo you want to repeat again? [Y/N] : ")
except:
    print("Invalid. Please try again.")
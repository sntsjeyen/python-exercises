distance = float(input("Distance Traveled (km)  :  "))
duration = float(input("Duration of Ride (min)  :  "))

int(float(distance))
int(float(duration))

rate = 60
added_rate = 4.50

total_added_rate_1 = distance * 4.50
total_fare_1 = rate + total_added_rate_1

two_minute = duration // 2
total_added_rate_2 = two_minute * 4.50
total_fare_2 = rate + total_added_rate_2

if total_fare_1 != total_fare_2:
    if total_fare_1 > total_fare_2:
        total_fare = total_fare_1
    elif total_fare_1 < total_fare_2:
        total_fare = total_fare_2
else:
    total_fare = total_fare_1

print("Total Fare \t\t:  Php {0:.2f}".format(total_fare))
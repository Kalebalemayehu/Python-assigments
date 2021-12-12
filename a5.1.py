#JTMS-14
#problem 5.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

#cups to liters
#gallons to liters
#gallon = 3.7854 liters
#cup = 0.2366 liters


def to_liter(gallon, cup):
     return (gallon * 3.7854) + (cup * 0.2366)

gallons= float(input("enter the number of gallons: "))
cups = float(input("enter the number of cups: "))

print("this is in liters", to_liter(gallons, cups))

    

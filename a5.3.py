#JTMS-14
#problem 5.3.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

#volume
#4/3πr3


import math

def givearea(r):
    return (4/3) * math.pi * (r*r*r)

Radius = float(input("enter the radius here: "))

print(givearea(Radius))



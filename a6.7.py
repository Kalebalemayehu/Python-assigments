#JTMS-14
#problem 6.7.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

biglst = []

number = int(input("enter number here: "))

while number != 0:
    biglst.append(number)
    number = int(input("enter number here: "))

print ("maximum number is", max(biglst),".")
print ("minumum number is", min(biglst),".")





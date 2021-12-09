#JTMS-14
#problem 7.5.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

tupplst = []

num = int(input("enter a number here: "))
while num >= 0:
    tupplst.append(num)
    num = int(input("enter a number here: "))

print(tupplst)

tupplst.reverse()

reversetup = tuple(tupplst)
print(reversetup)
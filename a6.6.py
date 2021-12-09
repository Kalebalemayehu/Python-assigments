#JTMS-14
#problem 6.6.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

def histogram(lst):
    for i in lst:
        print (i * "*")

n = int(input("enter len here: "))

demolst = [ ]

for i in range(n):
    demolst.append(int(input("enter a number here: ")))
    


histogram(demolst)


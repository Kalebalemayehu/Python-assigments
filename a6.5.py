#JTMS-14
#problem 6.5.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


def add(lst, val):
    addresult = [ ]
    for i in lst:
       addresult.append(i + val)
    return addresult

def multiply(lst, val):
    mulresult = [ ]
    for i in lst:
        mulresult.append(i * val)
    return mulresult

n = int(input("len of list: "))

inputlist = [ ]

for i in range(n):
    number = float(input("enter number here: "))
    inputlist.append(number)

print(inputlist)

print(add(inputlist, 1.5))
print(multiply(inputlist, 5))









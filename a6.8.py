#JTMS-14
#problem 6.8.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i ==j:
                return True
    return False

biglst = [ ]
biglst2 = [ ]

num = int(input("enter a number for list1: "))

while num >= 0:
    biglst.append(num)
    num = int(input("enter a number for list1: "))

num2 = int(input("enter a number for list2: "))

while num2 >= 0:
    biglst2.append(num2)
    num2 = int(input("enter a number for list2: "))



if overlapping(biglst, biglst2):
    print("The two lists are overlapping.")
else:
    print("The two lists are not overlapping.")








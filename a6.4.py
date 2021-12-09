#JTMS-14
#problem 6.4.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

filecall = input("enter the name here: ")

thefile = open('atexttocopy.txt', 'r')
riri = thefile.read()
print(riri)

copy = open('copy.txt', 'w')

copy.write(riri)

copy.close
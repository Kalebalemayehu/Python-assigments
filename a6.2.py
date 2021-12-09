#JTMS-14
#problem 6.2.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

numberfile = open('numbers.txt', 'r')

number = numberfile.readline()
sum = 0

while number != '' :
    sum = int(number) + sum
    number = numberfile.readline()

print(sum)

    



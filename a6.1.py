#JTMS-14
#problem 6.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


inputfile = open('letters.txt','r')
x = inputfile.read()
print (x)

pro = str(ord(x[0]) * ord(x[1]))

print(pro)

inputfile.close()

outputfile = open('output.txt', 'w')

outputfile.write(pro)


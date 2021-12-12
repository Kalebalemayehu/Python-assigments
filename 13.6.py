#JTMS-14
#problem 13.6.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de
import re

name = input("name the file with .txt: ")

file = open(name,  'r')






n = re.findall("[a-z]\.[a-z]{2,}@jacobs-university\.de", file.read())
print (n)

file.close()
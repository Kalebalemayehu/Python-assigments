#JTMS-14
#problem 5.6.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


#the program stops if no input in detected ie. string is empty

def count_vowels(s):
    num_vowels=0
    for i in s :
        if i in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels
        

str = input("enter something here: ")
while str != "":
    print (count_vowels(str))
    str = input("enter something here: ")

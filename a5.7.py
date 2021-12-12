#JTMS-14
#problem 5.7.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

a = int(input("enter a number here: "))
b = int(input("enter a number here: "))
s = input("enter a sentence or smtn here: ")
strlen = len(s)
lessthanlen = False

while not lessthanlen:
    if a >= 0 and a < strlen and b >= 0 and b < strlen :
        lessthanlen = True
    else:
        a = int(input("enter a number here: "))
        b = int(input("enter a number here: "))



print(s[a:b + 1])

##   print("Please enter a number ")
## check a & b < strl

##concat s & assign to a new string .. fn


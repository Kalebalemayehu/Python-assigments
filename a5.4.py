#JTMS-14
#problem 5.4.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

import random
random.seed
minval = 1
maxval = 5

r = random.randint(minval, maxval)
found = False

count = 0
while not found:
    count += 1
    guess = int(input("enter your guess here: "))
    if r == guess:
     print("you got it")
     found = True
     break
    elif guess < r:
      print("your guess is too small!", count, "time/s tried.")
    else:
     print("your guess is too high!", count, "time/s tried")
    

print("you tried", count, "times")





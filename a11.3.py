#JTMS-14
#problem 11.3.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

formula = input("input a space separated computation: ")

while formula != "quit":
    try:
        x = formula.split()
        if x[1] == '+':
            print (float(x[0]) + float(x[2]) )
        elif x[1] == '-':
            print (float(x[0]) - float(x[2]) )
        elif  x[1] == '*':
            print (float(x[0]) * float(x[2]) )
        elif x[1] == '/':
            print (float(x[0]) / float(x[2]) )
        formula = input("input a space separated computation: ")
    except ValueError:
        print ("that cant be done fam")
        formula = input("input a space separated computation: ")
    except IndexError:
        print(" i said SPACE separated computation idiot")
        formula = input("input a space separated computation: ")
        
    



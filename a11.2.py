#JTMS-14
#problem 11.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

while True:
    try:
        n = int(input("enter nummber :"))
        y = int(input("enter 2nd nummber :"))
        x = n / y
        print (x)
    
        n = ['x', 'f', '3', 'r', 'u']
        h = input("enter element to look up: ")
        y = n.index(h)
        
        x = "this is some string to split"
        a = int(input("enter number here: "))
        b = int(input("enter number here: "))
        print(x[a: b])

        

        break
    except ArithmeticError:
        print("Could not divide by zero")
    except ValueError:
        print("this isn't there bro")
    except TypeError:
        print("can't put that there bro")


    
    


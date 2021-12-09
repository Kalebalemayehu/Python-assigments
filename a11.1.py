#JTMS-14
#problem 11.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

while True:
    try:
        filename = input("Enter file name: ")
        thefile = open(filename, "r")
        break
    except:
        print("Could not open the file.")


cont = thefile.read()

print (cont)


    


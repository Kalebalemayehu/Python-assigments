#JTMS-14
#problem 7.8.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

def push(n, c):
    print("Pushing", c)
    n.append(c)

def pop(n):
    if (len(n) == 0):
        print("Stack underflow")
        return
    print("Popping element", n[-1]);
    return n.pop()

def empty(n):
    print("Emptying stack")
    for i in range(len(n)):
        pop(n)

stack = []

stinp = input("enter a charachter here: ")
while stinp != 'q':
    if stinp == 's':
        num = int(input("Enter a number: "))
        push(stack, num)
    elif stinp == 'p':
        pop(stack)
    elif stinp == 'e':
        empty(stack)
    stinp = input("enter a charachter here: ")

print("Good Bye!")







    
    






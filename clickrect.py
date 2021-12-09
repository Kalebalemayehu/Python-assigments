#JTMS-14
#problem 12.4.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

from graphics import *

def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

win = GraphWin()
a = win.getMouse()
b = win.getMouse()
rect = Rectangle(a, b)
w = abs(a.getX() - b.getX())
l = abs(a.getY() - b.getY())
rect.setOutline("red")
rect.setFill("red")
rect.draw(win)
# print (l)
# print (w)
print ("the area is", area(l, w))
print ("the perimeter is", perimeter(l, w))

win.getMouse()




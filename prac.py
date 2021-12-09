#JTMS-14
#problem 12.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


#rect = Rectangle(Point(30, 30), Point(70, 70))
from graphics import *


def main():
    win = GraphWin()
    shape = Rectangle(Point(20, 20), Point(120, 120))
    shape.setOutline("yellow")
    shape.draw(win)
    righteye = Circle(Point(60, 60), 10)
    righteye.setOutline("blue")
    lefteye = righteye.clone()
    lefteye.move(40, 10)
    righteye.draw(win)
    lefteye.draw(win)

    win.close()
main()
    

    
    
 
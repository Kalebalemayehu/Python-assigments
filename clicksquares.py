#JTMS-14
#problem 12.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


#rect = Rectangle(Point(30, 30), Point(70, 70))
from tkinter import Message
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(30, 30), Point(70, 70))
    shape.setOutline("green")
    shape.setFill("green")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newshape = shape.clone()
        newshape.move(dx, dy)
        newshape.draw(win)
        
    win.close()

main()
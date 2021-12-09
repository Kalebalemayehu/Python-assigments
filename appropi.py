#JTMS-14
#problem 12.5.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de
import random
from graphics import *

def isInCircle(x, y, d):
    return ((x - d/2)**2 + (y - d/2)**2) <= ((d**2) / 4) 

def approx(d, points):
    win = GraphWin()
    sq = Rectangle(Point(0, 0), Point(d, d))
    sq.setOutline("black")
    sq.draw(win)

    count = 0
    for i in range(1, points+1):
        x = random.randint(0, d)
        y = random.randint(0, d)

        if isInCircle(x, y, d):
            count += 1
            win.plotPixelFast(x, y, "red")
        else:
            win.plotPixelFast(x, y, "blue")
        
        if i % 100:
            print ("ratio =", 4 * count / i)

    win.plotPixel(d/2, d/2, "red")

    win.getMouse()

approx(100, 10000)
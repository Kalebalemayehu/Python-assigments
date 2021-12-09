#JTMS-14
#problem 12.3.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de
from graphics import *

def draw_archery():
    win = GraphWin()
   
    colors =  ["","blue", "black", "red"]
    for i in range (3,0, -1):
        shape = Circle(Point(50,50), i*20)
        shape.setOutline(colors[i])
        shape.setFill(colors[i])
        shape.draw(win)

    while win.getMouse().x < 100 and  win.getMouse().y < 100:
        continue
    win.close()

draw_archery()
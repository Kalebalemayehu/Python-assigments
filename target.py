#JTMS-14
#problem 12.3.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

from graphics import *

def draw_archery(lst):
    win = GraphWin()
    win.setBackground("grey")
   
    colors =  ["yellow" , "red", "blue", "black", "white"]
    for i in range (4, -1, -1):
        tuple1 = lst[i]
        shape = Circle(Point(tuple1[0], tuple1[1]), tuple1[2])
        shape.setOutline(colors[i])
        shape.setFill(colors[i])
        shape.draw(win)
    
    while win.getMouse().x < 100 and  win.getMouse().y < 100:
        continue
    win.close()

draw_archery([(100, 100, 15), (100, 100, 30),(100, 100, 45), (100, 100, 60), (100, 100, 75)])
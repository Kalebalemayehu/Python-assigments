#JTMS-14
#problem 12.2.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de
from graphics import *

win = GraphWin()
face = Circle(Point(80, 80), 50)
face.setOutline("yellow")

face.draw(win)
leftEye = Circle(Point (60 ,60), 5)
leftEye.setFill("yellow")
leftEye.setOutline("red")
rightEye = leftEye.clone()
rightEye.move(40, 0)
rightEye.draw(win)
leftEye.draw(win)
nosespot = face.getCenter()
# c = win.getMouse()
# d = win.getMouse()
nose = Polygon(nosespot , Point(75, 90), Point(85, 90))
nose.setOutline("yellow")
nose.setFill("green")
mouth = Rectangle(Point(65, 110), Point(95, 120))
tooth = Rectangle(Point(70, 115), Point(90,110 ))
leftear = Circle(Point(40, 40), 10)
leftear.setFill("yellow")
rightear = leftear.clone()
rightear.move(80, 0)
leftear.draw(win)
rightear.draw(win)
tooth.draw(win)
mouth.draw(win)
nose.draw(win)
win.getMouse()
win.close()       



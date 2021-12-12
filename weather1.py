#JTMS-14
#problem 13.2.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


import sys
import urllib.request





urlold = "https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp2008xx.csv"

A = "https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp2008"

B = input("enter a month(XX): ")

C = ".csv"

urlnew = A + B + C



sendto = 'w1data.csv'

try:
    x = urllib.request.urlretrieve(urlnew , sendto)
except:
    print("Error  fetching  URL: ", urlnew)
    sys.exit (1)






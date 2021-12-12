#JTMS-14
#problem 13.4.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

import sys
import urllib
import csv


url = 'https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp200811.csv'

f = open('wdata4.csv', 'w')
x = urllib.request.urlretrieve(url , f)
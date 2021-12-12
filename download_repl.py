#JTMS-14
#problem 13.5.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

import urllib.request
import sys
import csv
from os import replace


#exp200811.csv
url = 'https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp200811.csv'

addtoo = 'wdata24first.csv'
try: 
    sed = urllib.request.urlretrieve(url, addtoo)
except:
    print("erros fetching url: ", url)
    sys.exit(1)


fn = open('wdata24first.csv', 'r')
reader = csv.reader(fn)

fnn = open("wdata4.csv", 'w')
writer = csv.writer(fnn)

for row in reader:
    if reader.line_num ==2:
        fnn.write("modified the file with this text")
    else:
        writer.writerow(row)

fnn.close()
fn.close()


    




# # Read all data from the csv file.
# with open('exp200811.csv', 'rb') as b:
#      readfile = csv.reader(b)

# for line in readfile:
#     print (line)

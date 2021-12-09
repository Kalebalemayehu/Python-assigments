#JTMS-14
#problem 6.3.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


filename = input("enter something here: ")
inputwords = open('words.txt', 'r')

wordd = inputwords.readline()
count = 0

while wordd != '':
    count += 1
    nums = len(wordd.split())
    print('line', count, "has", nums, "words.")
    wordd = inputwords.readline()




    
    



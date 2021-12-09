#JTMS-14
#problem 7.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


def longest_word(lst):
    longestword = ''
    
    for word in lst:
        if len(word) > len(longestword):
            longestword = word
            
    lettlst = list(longestword)
    thelen = len(lettlst)      
    print("longest word is " + longestword + " and its length is "  + str(thelen) + ".")
            

    
Testlst = ['afuirgv', 'apple', 'something', 'lastthing']

longest_word(Testlst)

sentence = input("enter a sentence here: ")

forfun = sentence.split()

longest_word(forfun)



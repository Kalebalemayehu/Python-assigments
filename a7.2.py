#JTMS-14
#problem 7.2.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott","new":"nytt", "year":'\u00E5' + "r"}

#print('\u00E5')  #woaahhh

greeting = 'merry christmas and happy new year'
grenew = greeting.split()



def translate(list_en):
    swissgreet = []
    for i in grenew:
        swissgreet.append(dict[i])
    print (swissgreet)
        
            
    # swisent = " ".join(swissgreet) 
    # print(swisent)        
    # print(swissgreet)

        
        
            
            
    
translate(grenew)




    
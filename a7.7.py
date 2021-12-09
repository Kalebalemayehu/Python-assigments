#JTMS-14
#problem 7.7.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


sampleDict ={'Physics':  82, 'Math':  85, 'History':  75, 'Management':  70, 'Chemistry':  90}

testkey = input("enter a key here: ")



while testkey in list(sampleDict.keys()):
    print("this is there bruv.")
    break

else:
    print("this ain't there bruv.")   



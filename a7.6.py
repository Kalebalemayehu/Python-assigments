#JTMS-14
#problem 7.6.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de

sampleDict ={'Physics':  82, 'Math':  85, 'History':  75, 'Management':  70, 'Chemistry':  90}

def get_min(dict):  
    # grade = 101 
    # subject = "randomm"
    # for key, value in dict.items():
    #     if value <= grade:
    #         grade = value 
    #         subject = key
    #this is the harder way(didn't work yet)
    #butttt easier way to do it below!!!!!!!
  return  min(dict, key=dict.get)



print(get_min(sampleDict))


        




    
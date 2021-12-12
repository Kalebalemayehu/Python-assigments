#JTMS-14
#problem 13.1.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


import matplotlib.pyplot as plt

f1 = open("data.dat", "w")
x = []
y = []
for i in range (-20, 21):
    x.append(i)
    y.append(i**3)
    f1.write(str(i)+" "+" "+str(i**3)+"\n")

plt.plot(x, y)

plt.show()







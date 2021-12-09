#JTMS-14
#problem 7.4.py
#Kaleb Alemayehu
#kalemayehu@jacobs-university.de


n = 4

tuplst = []


count = 0
while count < n:
    tupinp = input("enter stuff for tup here: ")
    tupinp = tupinp.split()
    count += 1
    tuplst.append(tuple(tupinp))

print(tuplst)

# tuplst = [t for t in tuplst if t]


for i in range(n-1, -1, -1):
    if tuplst[i] == ():
        tuplst.pop(i)
        
print(tuplst)

    

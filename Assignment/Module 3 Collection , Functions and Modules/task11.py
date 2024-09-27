# Write a Python function that takes a list and returns a new list with unique elements of the first list.
    

u=[]                            # u empty dictionary 
l1=input("Enter Number separted by space : ").split()       # l1 input enter number seprated by space and last .split() that mean every list in this is diffrent list 

for i in l1:            # for i in l1
    if i not in u:          # if i not in u 
        u.append(i)         # then u input append(i)

print(u)            # then print unique list  


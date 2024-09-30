# Write a Python program to remove an empty tuple(s) from a list of tuples. 


l = [(1,2,3) , () , (4,5,6) , () , (7,8,9) , ()]        # list all number 

l1 = []                                             # empty list 

for i in l:                                         # for i in l 
    if i:                                                   # if i 
        l1.append(i)

print()
print("list : ",l)                              # list original 
print()
print("Remove after empty tuple : ",l1)         # print remove after empty tuple
print()
# Write a Python program to replace last value of tuples in a list. 

t = [(1,2,3) , (5,6,7) , (8,56,3) ]         # tuple in list 

nv=20                                       # new value 20 

tl=[(a,b,nv) for a,b,c in t]                # tuple list a,b,newvalue  for a,b,c in t 

print("Updated list of tuple : ",tl)        # print updated list of tuple t1



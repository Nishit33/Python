# Write a Python program to check whether an element exists within a tuple. 

t=(4,6,8,9,4,2,3,1,4)                           # tuple number 

eleme=int(input("Enter number to check : "))        # elements int input enter number to check 

if eleme in t:                              # if elements in t then print  exists in the tuple 
    print("Exists in the tuple ")

else:                                           # else does not exists in the tuple 
    print("Does not exists in the tuple !!!")    
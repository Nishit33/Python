# Write a Python program to map two lists into a dictionary 

   
l1 = [1, 2, 3, 4]
l2 = [ "Hello", 8, 5 , "Hey" ]

    
d = {}

    
for i in range(len(l1)):
    d[l1[i]] = l2[i]
    
print(d)

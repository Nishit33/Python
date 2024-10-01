# Write a Python script to concatenate following dictionaries to create a new one.

   
s1 = {1 : "Hello", 2 : "Welcome", 3 : "Sun"}          # Dictionaries
s2 = {4 : 4.4, 5 : 6, 6 : 8.7}

d ={}
    
for i in (s1,s2):               # for loop to concat string in empty dictionary d.update(i)
    d.update(i)
    
print(d)                        # then print d 
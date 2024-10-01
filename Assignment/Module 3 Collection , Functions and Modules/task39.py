# Write a Python program to print all unique values in a dictionary.

  
d = {'a': 200, 'b': 100, 'c': 100, 'd': 200, 'e': 300}            # Dictionary

ul = []     

   
for i in d.values():             # store unique Values in unique list
    if i not in ul:
        ul.append(i)
    
print(ul)
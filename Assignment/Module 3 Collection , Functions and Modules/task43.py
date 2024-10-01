"""
 Write a Python program to create a dictionary from a string. 
 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 

"""

s = input("Enter a String : ")      # enter string 

d = {}                          # empty dictionary 

for i in s:                         # for i in string
    if i in d:                  # for i in dictionary 
        d[i] += 1                                   # d[i] + = 1 
    else:
        d[i] = 1                # else d[i] = 1
        
print(d)            # print d
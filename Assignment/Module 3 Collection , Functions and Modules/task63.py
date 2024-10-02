# How Do You Traverse Through A Dictionary Object In Python? 
"""
To traverse through a dictionary object in Python, you can use several methods depending on what you need to access (keys, values, or both). 
Below are some common ways to traverse a dictionary:
"""



"""
1. Traversing Keys
You can iterate over the dictionary's keys using a simple for loop:
"""

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

for key in my_dict:
    print(key)




"""
2. Traversing Values
You can iterate over the dictionary's values using the values() method:

"""
for value in my_dict.values():
    print(value)




"""
3. Traversing Keys and Values
You can traverse both keys and values using the items() method, which returns key-value pairs as tuples:
"""
for key, value in my_dict.items():
    print(key, value)




"""
4. Traversing in a Specific Order
If you want to traverse the dictionary in a sorted order of keys:
"""
for key in sorted(my_dict):
    print(key, my_dict[key])

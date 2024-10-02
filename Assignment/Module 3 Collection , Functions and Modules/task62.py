# How will you create a dictionary using tuples in python?

"""
You can create a dictionary using tuples in Python by passing a list of tuples to the dict() constructor. 
Each tuple should contain exactly two elements: the first element will be the key,
and the second element will be the value.
"""


tuple_list = [('apple', 3), ('banana', 5), ('orange', 2)]       # tuple list 


fruit_dict = dict(tuple_list)           # tuple convert into  dictionary 


print(fruit_dict)                       # print dictionary 

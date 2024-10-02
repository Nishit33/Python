# Why Do You Use the Zip () Method in Python? 

"""
The zip() function in Python is used to combine two or more iterables such as lists, tuples, etc.
into a single iterable of tuples. Each tuple contains elements from the corresponding position of the input iterables.


"""
names = ['Alice', 'Bob', 'Charlie']             # list all name 
scores = [85, 90, 95]                           # score list all number 

combined = zip(names, scores)           # combined = zip(names , scores)

print(list(combined))           # print list combined

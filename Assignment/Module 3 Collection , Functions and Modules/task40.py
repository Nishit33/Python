"""
Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']}
"""

data = {'1': ['a', 'b'], '2': ['c', 'd']}     # data dictionary

    
l1 = data['1']  # list 1 data 
l2 = data['2']  # list 2 data

for i in l1:                # for i in list 1 
    for j in l2:            # for j in list 2 
            print(i+j)        # print i + k + j 
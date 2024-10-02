# How Do You Check The Presence Of A Key In A Dictionary? 

"""
In Python, you can check the presence of a key in a dictionary using the in keyword. 
This is the most common and efficient method. Here are different ways to check if a key exists in a dictionary:
"""

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}            # dictionary key and values

# Check if 'apple' is a key in the dictionary
if 'apple' in my_dict:                                  # if apple in dictionary then print key exists
    print('Key exists!')
else:                                                   # otherwise does not exist
    print('Key does not exist.')





# Using get() to check for the key
value = my_dict.get('banana')

if value is not None:                                   # if value is not none print key exists 
    print('Key exists!')
else:
    print('Key does not exist.')                        # otherwise key does not exist 





if 'orange' in my_dict.keys():                          # if orange in dictionary.keys then print key exists
    print('Key exists!')
else:
    print('Key does not exist.')                        # otherwise print key does not exist 
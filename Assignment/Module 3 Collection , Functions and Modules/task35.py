# Write a Python program to check multiple keys exists in a dictionary 


d = {'apple': 50, 'banana': 20, 'orange': 30, 'mango': 10}      # dictionary key and value 


keys = ['apple', 'banana']                                  # keys 


exist = all(key in d for key in keys)                   # exist all key in dictionary for key in keys


if exist:                                               # if exist then print all key exist 
    print("All keys exist in the dictionary.")
else:                                                       # otherwise key is not in ditionary 
    print("Some keys are missing in the dictionary.")

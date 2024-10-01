# Write a Python script to check if a given key already exists in a dictionary. 

  
d = {'A': 44, 'B': 2, 'C': 13, 'D': 3, 'E': 12, 'F': 69, 'G' : 50}    # dictionary


key = input("Enter Key : ")                                 # enter key 


if key in d:                                            # if key in dictionary 
    print(f"Key {key} exist in dictionary.")            # print key is exist in dictionary 
else:
    print(f"Key {key} does not exist in dictionary.")    # else key deos not exist in dictionary 
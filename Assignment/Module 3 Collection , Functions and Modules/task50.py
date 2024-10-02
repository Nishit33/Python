# Write a Python program to read a random line from a file. 

import random

file = open("test123.txt", "r")     # file open which file paste path location 

    
lines = file.readlines()            # lines = file.readlines()

    
if lines:                               # if lines :
    
    random_line = random.choice(lines)      # random_line = random.choice(lines)

    print("Random line : ", random_line)  # Print the line without trailing newline

else:
    print("The file is empty.")     # else otherwise file is empty 

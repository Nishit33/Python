#  Write a Python program to read a file line by line and store it into a list 

with open('test1.txt','r') as file:         # with open file name as file 

    lines = file.readlines()                # lines =  file.readlines()

print(lines)                                #  and then print lines all value in list form 

#  Write a Python program to read last n lines of a file. 

file = open('test1.txt','r')        # file open and put file location 

line = file.readlines()             # line = file.readlines()

n = 3                               # last 3 line 

for i in line[-n:]:                 # loop for i in line [-n:] that mean reverse 
    print(i.strip())                # print(i.strip())


file.close                          # and then file close 

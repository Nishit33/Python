#  Write a Python program to read a file line by line store it into a variable. 

lines = []      # empty 

with open('test1.txt' , 'r') as file:           # with open file name , r as file 

    for i in file:                              # for i in file 
        lines.append(i.strip())                # lines.append(i.strip())

for i in lines:                             # then one more loop for i in lines: and print i 
    print(i)


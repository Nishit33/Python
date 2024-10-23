#  Write a Python program to write a list to a file. 

l = ["This is New" , "File Add" , "Into List" , "Done"]         # list this is all separate string word 

with open('test1.txt','w') as file:                     #  with open file name as file 
    for i in l:                                             # for i in list: then file.write(i + '\n')
        file.write(i + '\n')
#  Write a Python program to count the number of lines in a text file. 


count = 0                               # count = 0 

with open('test1.txt','r') as file:             # with open file name as file and then loop 

    for i in file:                              # for i in file count +=1 how many line in file 
        count+=1

print("The Total Number is : ",count)        # and then print file count number 
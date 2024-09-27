#  Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.

l=[]        # empty dictionary 

for i in range(1,31):           # for i in range (1,31) 
    if i<6 or i>25:             # if i<6 or i>25 
        l.append(i*i)           # l.append(i*i)

first_5 = l[:5]         # first five elements start with 0 and end with 5 number 

last_5 = l[-5:]     # last five elements start with with 25 and end with 30 number 

print("First 5 elements : ",first_5)        # print first five elements 

print("Last_5 elements : ",last_5)          # print last five elements 


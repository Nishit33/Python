# Write a Python program to sum of three given integers. However, 
# if two values are equal sum will be zero.

a=int(input("Enter Number 1 : "))       # a input number 
b=int(input("Enter Number 2 : "))       # b input number 
c=int(input("Enter Number 3 : "))       # c input number 


if a==b or b==c or a==c:        # if a==b b==c and a==c print 0
    print("0")

else:                       # else print a+b+c sum 
    print(a+b+c)    

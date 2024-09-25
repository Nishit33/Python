# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.

a = int(input("Enter Number 1 : "))     # number input a
b = int(input("Enter Number 2 : "))     # number input b


if a==b or a+b==5 or a-b==5 :           # if a==b , a+b=5 , a-b=5 
    print("True")                       # return type true

else:                   # else 
    print("False")    # false


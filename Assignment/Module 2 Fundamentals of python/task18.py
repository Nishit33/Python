"""
 Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string. 

"""

def new(s):         # def new(s) function
    if len(s)<2:            # if length of s less than 2
        return ""           # return ""
    return s[:2] + s[-2:]           # return first 2 char and last 2 char 


string = input("Enter string : ")       # string input enter string 
print("Result :",new(string))           # print new function string 
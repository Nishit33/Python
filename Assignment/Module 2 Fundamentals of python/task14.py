# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

s1 = input("Enter String 1 : ")     # enter string 1 
s2 = input("Enter String 2 : ")     # enter string 2

if len(s1) < 2 or len(s2) < 2 :         # if length of string 1 < 2 or length of string 2 < 2 
    print("both string must have 2 characters.")        # print both string must have 2 char 

else:                           
    ns1 = s2[:2] + s1[2:]       # news1 = s2[:2] + s1[2:] 
    ns2 = s1[:2] + s2[2:]       # news2 = s1[:2] + s2[2:] 

    print(ns1 + " " + ns2)      # print ns1 + " " + ns2

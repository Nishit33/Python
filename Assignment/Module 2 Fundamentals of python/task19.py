"""
 Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string.

"""

s = input("Enter a string: ")       # s input enter string

s1 = s.find("not")              # s1 s.find("Not")
s2 = s.find("poor")             # s2 s.find("poor")


if s1!=-1 and s2!=-1 and s1<s2:         #if s1 not equal to -1 and s2 not equalto -1 and s1 less then s2 
    result=s[:s1]+"good"+s[s2 + 4:]     # result = s[:s1] + "good" + s[s2+4:]

else:                   # else result = s
    result = s

print("String is: ",result)       # print string is result 
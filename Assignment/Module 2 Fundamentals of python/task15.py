"""
 Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged. 

"""


n = input("Enter String : ")        # n input string 

if len(n)>3:                # if length of > 3 
    if n.endswith('ing'):       # if n.endswith last ing then add ly in end of string 
        n1= n + 'ly'

    else:                      # else n1 = n + ing add end of string 
        n1 = n + 'ing'    

else:                               # n1 = n same leave it dont change 
    n1 = n

print("string is : ",n1)            # print string n1
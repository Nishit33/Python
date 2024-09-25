# Write a Python program to count occurrences of a substring in a string. 

n = input("Enter String : ")        # enter string 
n1 = input("Enter Substring : ")        # n1 input substring 

s=0             # start point 
e=0                 # end point 

while s < len(n) :          # while s < length of (n)
    p=n.find(n1,s)          # p = n.find n1 and s

    if p!=-1:       # if p not equal to -1 
        e+=1        # end point + 1
        s=p+1       # s point p + 1

    else:       # else break
        break


print("Number count occurences : ",e)           # number of count e 






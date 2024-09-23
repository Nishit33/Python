# Write a Python program to count the number of characters (character frequency) in a string

n =input("Enter string : ")     # enter string 

d ={}               # empty dictionary

for i in n:         # for i in n 
    if i in d:      # if i in d print d[i] +=1
        d[i]+=1

    else:       # else d[i]=1
        d[i]=1

print(d)            # print d

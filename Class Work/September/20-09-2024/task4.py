
# User input list and order asc and desc and find out which is small number and which is largest number and second largest 

n=int(input("Enter Length of list : "))     # user input how many length of list 

l = []                                      # empty list 

for i in range (1,n+1):                         # for loop start with 1 and going with n+1 
    n1=int(input("Enter Elements : "))      # second variable n1 input elements

    l.append(n1)                    # l.append is n1 that mean whatever we input n1 that append in l 

print(l)                    # after print l all list data show 

for i in range(0,len(l)):               # for loop start with 0 and goes like len(l)
    for j in range(i+1,len(l)):     # second loop was i+1 and len(l)
        if l[i]>l[j]:                       # if l[i] > l[j]
            temt = l[i]             # temt file through change 
            l[i] = l[j]
            l[j] = temt


l2 = []                             # l2 empty list

for i in range(0,len(l)):                   #for loop 0 and len(l)
    print(l[i])                     # print(l[i])
    l2.append(l[i])                 #l2.append (l[i]) 

print(l2)                   # print(l2) that we creat empty list 


print("small : ",l2[0])             # small number find out l2[0] 
print("Large : ",l[-1])         # large number l[-1] that mean revers 
print("second large : ",l[-2])      #second large l[-2] 


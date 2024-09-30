# Write a Python program to check whether a list contains a sub list 

list=input("Enter Main List : ")        # main list enter list 

sublist=input("Enter sublist : ")       # enter sublist 

if all(i in list for i in sublist):     # for all i in list for i in sublist to check the exist or not 
    print("Sublist is exist")

else:
    print("Sublist is Notexist")



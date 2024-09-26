# Write a Python function that takes two lists and returns true if they have at least one common member.

def value(list1,list2):         # function create list1 and list2 
    for i in list1:             # for i in list1 if i in list2 return true 
        if i in list2:
            return True             
        return False               # otherwise return false 


list1 = input("Enter List1 Number : ")      # list1 input enter number 
list2 = input("Enter List2 Number : ")       # list2 input enter number 

result = value(list1,list2)     # result = values list1 , list2

print(result)               # print result 


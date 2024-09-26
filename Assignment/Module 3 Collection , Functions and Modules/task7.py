#  Write a Python program to remove duplicates from a list. 

list1 = [1,2,3,4,5,5,4,3,2,6,7,8,3,4,5,9]       # list 1 

list2=[]                                    # list2 empty 

for i in list1:                     # for i in list1 
    if i not in list2:          # if i not in list2 so then list2.append(i) add list2
        list2.append(i)

print("Remove dupilcate number : ",list2)       # print remove duplicate number and print list2

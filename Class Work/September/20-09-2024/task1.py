
# List in Python 

l = [2,3,2,56,65,6.7,32,2,122,"Nishit",9,True]

print(l)

l.append()  # in list last value add with in .append()

l.clear()   # All list clear 

l.copy()        # All list copy to another list 

l2 = l.count(2)      # Count which is

l.extend([20,30,45,60])     # Multipule value add in list use extend 
print(l)        

l.insert(1,'India')        # Insert index number 1 put another string and number
print(l)

l.pop(3)         # Bydefalut remove last character otherwise we can pass argument index number that will be remove
print(l)


l.remove(122)       # Remove list number whatever we delet input in argument 
print(l)

l.reverse()         # All list data reverse 
print(l)


l1 = [32,54,76,87,98,32,546,7643,12,44]     # All list data same data type value sort like ASC
l1.sort() 
print(l1)


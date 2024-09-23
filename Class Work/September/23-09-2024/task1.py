# Tuple in python

t = (1,2,53,65.43,"Done",43,66,1,34,54,True,34)

print(type(t))          # find out type

print(t)

print(t.count(34))      #how many times this value in tuple

print(t.index(65.43))       # which number in index 


l = list(t)         # convert tuple into list 

l.extend([100,200,300,400,500])     #list extend add value
print(l)


t1=tuple(l)             # new variable t1 list to tuple
print(t1)
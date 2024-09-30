# Write a Python program to find the repeated items of a tuple. 

t = (1,3,5,2,"Virat",6,7,"Ronaldo","suiiiiii",9,8,"Ronaldo")        # tuple all list 

count = {}                                                         # empty dicionary 

for i in t:                                                     # for i in t
    if i in count:                                                  # if i in count 
        count[i]+=1                                                 # count[i] += 1

    else:                                                       # else count[i]=1
        count[i]=1    

repeat = [i for i , count in count.items() if count>1]              # repeat i for i count in count.items() if count >1 then print 

print("Tuple : ",t)                                     # all tuple print 

print("Repeated items in tuple is : ",repeat)           # repeated items print tuple 

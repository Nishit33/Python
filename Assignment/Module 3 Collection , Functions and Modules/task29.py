# Write a Python program to unzip a list of tuples into individual lists. 

l = [(1,2,3) , (7,8,9) , ("Kohali","Ronaldo","CR7")]        # list of tuple 

l1 , l2 , l3 = [list(t) for t in l]                     # make a new varible l1 ,l2,l3 

print(l1)                                   # and all print l1 l2 l3 
print(l2)
print(l3)

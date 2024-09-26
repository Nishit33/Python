# Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given 
# list of strings. 



l = input("Enter strings separated by space: ").split()     # we asking for list and .split() to diffrent in list 

count = 0                                               # count 0 

for i in l:                                                         # for i in l 
    if len(i) >= 2 and i[0] == i[-1]:      # if length of l greter than 2 and i[0] == i[-1] that mean first and last letter is same
        count += 1                         # so count is 1 

print("Number of strings count is :", count)        # and print count number 


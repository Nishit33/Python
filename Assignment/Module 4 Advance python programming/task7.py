#  Write a python program to find the longest words. 

ask = "Python is great language "   # store string in varible

word = ask.split()          # word = ask.split() every word is split in list 

longest = ""                # longest =""
max_length = 0              # max length = 0

for i in word:                      # for i in word we can create loop if len(i) > max length 
    if len(i) > max_length:                 # so max length = len(i)
        max_length = len(i)
        longest = i                     # longest = i 



print("The longest word is : ",longest)         # and then print the longest word is 
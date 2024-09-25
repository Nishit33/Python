# Write a Python program to count the occurrences of each word in a given sentence

n = input("Enter String : ")    # input string 

words = n.split()           # word = n.split()

word_count={}           # word count = empty dictionary 

for i in words:             # for i in words
    if i in word_count:         # if i in wordcount 
        word_count[i]+=1        # then print wordcount +=1

    else:
        word_count[i]=1         # else wordcount = 1

for i, count in word_count.items():     # for i count in wordcount . items()
    print(i,":",count)              # print i : count how many times in string 
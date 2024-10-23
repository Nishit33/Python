#  Write a Python program to count the frequency of words in a file. 

word_count = {}                             # word count = {} dictionary 

with open('test1.txt','r') as file:         # with open file name as file 

    for line in file:                       # then create for loop and words variable store in line.split () that is seprate in list 

        words = line.split()
        
    
        for word in words:                  # for word in worrds that mean we sepret all list string we can all string in lower case 
            word = word.lower()  
            if word in word_count:              # then create loop again word in empty dictionary 
                word_count[word] += 1           # word_count[word] += 1 all string word is 1 and if repeat then plus 1 
            else:                               # else as it is only one show 
                word_count[word] = 1  


for word, count in word_count.items():      # for word , count in word_count.items()
    print(f'{word}: {count}')                   # print word and count 


#Write a Python function that takes a list of words and returns the length of the longest one.


def long(words):        # function name long(words)
    l=0                 # length = 0

    for word in words:          # for word in words if len(word) > length

        if len(word)>l:
            l = len(word)       # l = length of word 

    return l            # return length


out = input("Enter list separated by spaces : ").split()    # out input space list 

print("The longest of word from words in : ",long(out))     # print long word and call function 
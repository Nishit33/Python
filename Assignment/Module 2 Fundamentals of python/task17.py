#  Write a Python function to reverses a string if its length is a multiple of 4.

def reverse(s):         # function reverse (s)
        l=0             # length = 0
            
        if len(s) %4 == 0:          # if length of s % 4 == 0 that mean user input 4 number string then do reverse
                return s[::-1]          # reverse -1
        
        else:               # else string length is more than 4 
           return "length of String is not a multiple of 4."


str = input("Enter a string : ")        # str input enter a string
print(reverse(str))         # print reverse(str)
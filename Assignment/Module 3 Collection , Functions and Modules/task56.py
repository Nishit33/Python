# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

    
l = [123.4, 32.22, 93.85, 104.86, 53.62, 74.58, 61.47, 130.658, 121.94, 251.77]         #list of decimal numbers

    
max = l[0]                  # max length = 0
min = l[0]                  # min length = 0 

    
for i in l:                         # for i in list 
        
    if i > max:                     # if i greter than max so max = i 
        max = i
        
    else:                          # else i less than min so min = i              
        i < min
        min = i

print("Maximum number:", max)       # print maximum number 
print("Minimum number:", min)       # print minimum number 
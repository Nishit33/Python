# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def factorial(n):                                       # create function factorial
        
    if n < 0:                                               # if n < 0  return "Not find factorial for negative number "
        return "Not find Factorial for negative numbers."
    
    elif n == 0:                                        # elif n == 0 return 1 
        return 1
    
    else:                                           # else fact=1 
    
        fact = 1
        for i in range(1, n + 1):                   # for i in range (1,n+1)
            fact *= i                           # fact*=i
        return fact                                 # return fact

    
n = int(input("Enter a integer: "))                     # user asking integer number 

print(f"The factorial is : {factorial(n)}")             # print factorial number 
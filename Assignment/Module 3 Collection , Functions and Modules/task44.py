# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def factorial(n):
        
    if n < 0:
        return "Not find Factorial for negative numbers."
    
    elif n == 0:
        return 1
    
    else:
    
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    
n = int(input("Enter a integer: "))

print(f"The factorial is : {factorial(n)}")
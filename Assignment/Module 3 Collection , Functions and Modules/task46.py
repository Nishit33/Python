# Write a Python function to check whether a number is perfect or not. 

def perfect_number(n):
    
    sum = 0

        
    for i in range(1, n):
        if n % i == 0:
            sum += i

        
    if sum == n:
        print(f"{n} perfect number.")
    else:
        print(f"{n} Not perfect number.")
    
    

n = int(input("Enter a number: "))

    
perfect_number(n)           # function call

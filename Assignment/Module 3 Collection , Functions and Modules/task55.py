# Write a Python program to returns sum of all divisors of a number 

n = int(input("Enter a Number : "))

sum = 0
  
for i in range(1,n+1):
    if n % i == 0:
        sum += i
        
print("The sum of all divisors of : ",sum)

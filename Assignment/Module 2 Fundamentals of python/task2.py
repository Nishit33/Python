#  Write a Python program to get the Factorial number of given number.

n = int(input("Enter Number : "))       # input number factorial 

fact=1                  # fact declar

for i in range(1,n+1):          # loop to going n value 
    fact*=i                 # fact *=i

print(fact)             # and then print fact
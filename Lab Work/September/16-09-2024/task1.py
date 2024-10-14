
# Fibonacci series Using for loop

n1 = 0
n2 = 1
n3=0

n= int(input("Enter Number for fibonacci series : "))

print(n1)
print(n2)

for i in range(3,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)

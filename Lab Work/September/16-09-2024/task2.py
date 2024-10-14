

# Fibonacci series Using While loop

n1 = 0
n2 = 1
n3=0
i=2


n = int(input("Enter Number for fibonacci series : "))

print(n1)
print(n2)

while(i<n):
    n3=n1+n2
    n1=n2
    n2=n3
    i+=1

    print(n3)
    



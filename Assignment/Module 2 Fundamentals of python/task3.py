#  Write a Python program to get the Fibonacci series of given range. 

n = int(input("Enter Number : "))  # input number 

n1=0        # alredy show n1 = 0
n2=1        # n2 = 1

print(n1)       # print n1
print(n2)       # print n2

for i in range(3,n+1):      # for loop start with 3 and going n+1
    n3=n1+n2        # n3 = n1+n2
    n1=n2           # n1=n2
    n2=n3           # n2=n3
    print(n3)       # print n3

    


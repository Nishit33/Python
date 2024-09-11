

# prime number find out 

# function without parameter and without return  

# function with parameter and without return 


def myprime(n):
    
    c=0

    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        print("Prime")

    else:
        print("Not prime")    


# n = int(input("Enter Number : "))
myprime(7)        
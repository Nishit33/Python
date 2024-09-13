
# package  

def add():
    a=int(input("Enter Number : "))
    b=int(input("Enter Number : "))

    print("Addition : ",a+b)


def fact():
    n=int(input("Enter Number : "))

    fac=1

    for i in range(1,n+1):
        fac*=i

    print(fac)    


def prime():

    n=int(input("Enter Number : "))

    c=0

    for i in range(1,n+1):
        if n%i==0:
            c+=1

    if c==2:
        print("prime")        

    else:
        print("Not Prime")    


def right():
    for i in range(1,6):
        print("*"*i)


def left():
    for i in range(1,6):
        print(" "*(6-i),"*"*i)


def Triangle():
    for i in range(1,6):
        print(" "*(6-i)," *"*i)


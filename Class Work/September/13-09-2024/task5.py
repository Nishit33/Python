
# FUNCTION WITH PARAMTER AND WITH RETURN

def fact(n):
    

    fac=1
    for i in range (1,n+1):
        fac*=i

    return fac    


n=int(input("Enter Number : "))
print(fact(n))        
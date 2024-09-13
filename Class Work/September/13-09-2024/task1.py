
# FUNCTION WITHOUT PARAMTER AND WITH RETURN TYPE


def fact():

    n=int(input("Enter Number : "))

    fac=1

    for i in range(1,n+1):
        fac*=i

    return fac    



print(fact())
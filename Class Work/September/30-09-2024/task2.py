# indexing error 

try:
    l = [1,2,3,4]
    n = int(input("Enter Index Number : "))

    print(l[n])
except ValueError as e:
    print(e)    

except IndexError as e:
    print(e)    



# prime number find out

c=0

n=int(input("Enter Number : "))

for i in range(1,n+1):
    if n%i==0:
        c+=1

if c==2 :
    print("Prime!")       

else:
    print("Not Prime!")

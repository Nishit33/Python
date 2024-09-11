# 5 user input and check odd or even 

ev_count=0
odd_count=0

evencount=0
oddcount=0

for i in range(1,6):
    n = int(input("Enter Number : "))
    if n%2==0:
        print(n,"even")
        ev_count += 1
        evencount=evencount+n

    else:
        print(n,"odd")    
        odd_count += 1
        oddcount=oddcount+n
print()
print("evencount is : ",ev_count)    
print("oddcount is : ",odd_count)   
print()
print("Even count total sum is : ",evencount)
print("Even count total sum is : ",oddcount)

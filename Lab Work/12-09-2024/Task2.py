
# 5 number ask for user and check odd or even 

evencount=0
oddcount=0
even=0
odd=0

for i in range (1,6):       # This is for loop asking 5 number 
    n=int(input("Enter Number : "))         

    if(n%2==0):
        print("Even!!")
        evencount=evencount+n
        even+=1


    else:
        print("Odd!")    
        oddcount=oddcount+n
        odd+=1

print("Total Even number is : ",even)
print("Total Odd number is : ",odd)

print("Total Even sum is : ",evencount)
print("Total Odd sum is : ",oddcount)

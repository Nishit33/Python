# Exception handling

try:
    a = int(input("Enter Number : "))
    b = int(input("Enter Number : "))

    print("Addition : ",a+b)

except ValueError as e:
    print(e)    


else:
    print("Try & else are excuted!!")

finally:
    print("Thank You")
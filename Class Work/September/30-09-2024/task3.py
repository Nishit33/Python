try:
    n = int(input("Enter NUmber : "))
    n1 = int(input("Enter NUmber : "))

    print("Divison : ",n/n1)

except ValueError as e:
    print(e)    

except ZeroDivisionError as e:
    print(e)
    

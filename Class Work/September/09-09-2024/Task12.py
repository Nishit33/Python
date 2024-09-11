count = 0
Total = 0
while(True):
    print(" Please Select Cinema Theater!")
    print("1 PVR Cinema")
    print("2 Cinemax")
    print("3 Imax")
    print("4 Rajhansh Cinema")
    print()

    choice = int(input("Enter Your Choice: "))
    
    if (choice == 1):
        print("\nYeah, You Selected PVR Cinema!\n")
        print("Please Select Ticket!")
        print("1 Normal    RS 180")
        print("2 Silver    RS 220")
        print("3 Gold      RS 350")
        
        ticket = int(input("Please Select Ticket: "))
        if (ticket == 1):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n * 180
            print(f"So, Bill is: {count}")
            
        
        elif (ticket == 2):
            print()

            n = int(input("Enter Ticket Quantity: "))
            count = n*220
            print(f"So, Bill is: {count}")
            

        else:
            print()

            n = int(input("Enter Ticket Quantity: "))
            count = n*350
            print(f"So, Bill is: {count}")
            

    elif (choice == 2):
        print("\nYeah, You Selected Cinemax!\n")
        print("Please Select Ticket!")
        print("1 Normal    RS 190")
        print("2 Silver    RS 230")
        print("3 Gold      RS 330")
        
        ticket = int(input("Please Select Ticket: "))
        if (ticket == 1):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*190
            print(f"So, Bill is: {count}")
            
        elif (ticket == 2):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*230
            print(f"So, Bill is: {count}")
            
        else:
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*330
            print(f"So, Bill is: {count}")
            

    elif (choice == 3):
        print("\nYeah, You Selected Imax!\n")
        print("Please Select Ticket!")
        print("1 Normal    RS 350")
        print("2 Silver    RS 490")
        print("3 Gold      RS 750")
        
        ticket = int(input("Please Select Ticket: "))
        if (ticket == 1):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*350
            print(f"So, Bill is: {count}")
            
        elif (ticket == 2):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*490
            print(f"So, Bill is: {count}")
            
        else:
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*750
            print(f"So, Bill is: {count}")
            

    elif (choice == 4):
        print("\nYeah, You Selected Rajhansh!\n")
        print("Please Select Ticket!")
        print("1 Normal    RS 230")
        print("2 Silver    RS 340")
        print("3 Gold      RS 450")
        
        ticket = int(input("Please Select Ticket: "))
        if (ticket == 1):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*230
            print(f"So, Bill is: {count}")
            
        elif (ticket == 2):
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*340
            print(f"So, Bill is: {count}")
            
        else:
            print()
            n = int(input("Enter Ticket Quantity: "))
            count = n*450
            print(f"So, Bill is: {count}")
            
    else:
        print("Invalid Choice Please Try Again")
        break


    Total = Total + count

    print()
    print("Your Bill Total is : ",Total+0.9)


    order = input("Do you want more orders? Yes/No: ")
    if (order == 'N' or order == 'n'):
        print("You are Exit!!!")
        break
    else:
        continue
        

# Core Python Assessment Test Fruit manager mask

d = {}                      # empty dictionary

menu="""                    

            WELCOME TO FRUIT MARKET 

            1) MANAGER
            2) CUSTOMER 
            
        
        """

print(menu)                 # print menu 

roll=int(input("Select Your Role : "))          # slect your roll choose manager or customer


def market(n):          # function create
    while True:         # while loop infinite
        
      
        if roll==1:         # if roll==1 manager 
            fmm="""

        Fruit Market Manager 

        1) Add Fruit Stock
        2) View Fruit Stock
        3) Update Fruit Stock
            
        """

            print(fmm)          # print add fruit , view stock and update fruit stock 

            choice=int(input("Enter Your Choice : "))       # choice in fruit market manager 

            if choice==1:                                   # if choice == 1 add fruit stock 
                print("Add Fruit Stock")
                fruit=input("Enter Fruit Name : ")          # enter name fruit name 
                qun=int(input("Enter Quantity (in Kg) : "))     # enter quantity fruit
                price=int(input("Enter Price : "))          # enter price 


                d[fruit] = {'qty' : qun , 'Price' : price}      # saved in dictionary d[fruit] = {qty : qun  ,  price : price}


            elif choice==2:                                 # elif choice 2 view fruit stock 
                if d:                                       # if dictionary value then print d 
                    print(d)
                   
                else:                                       # else print no stock 
                    print("No stock!")    


            elif choice == 3:                               # elif choice == 3 fruit input enter fruit name 

                fruit = input("Enter Fruit name : ")        

                if fruit in d:                          # if fruit in dictionary then move ahed and ask 
                    qun=int(input("Enter new quantity : ")) # qun ask new quantity 
                    price=int(input("Enter new price : "))  # price ask new price 

                    d[fruit] = {'qty' : qun , 'Price' : price}  # same as saved is upper so value is overwrite 
                    print()
                    print("Stock Updated!!")            # stock updated 
                    print()

                else:                                    # if fruit is not stock then print not stock in please add first 
                    print("This fruit is not in stock please add first!!")    

            else:                       # invalid input number 
                print("Invalid Input!!")
                break

        else:
            print("Invalid input")    
            break


        print()
        final=input(("Do You Want to perform more operation (press y for yes) (n for no) : ")).lower() # asking for do you want to perform more operation

        if final == 'y':        # if yes then continue
            continue

        elif final == 'n':      # elif no then break the loop and show msg thank you 
            print("Thank You!!")
            break

        else:                   # else invalid character then break the loop 
            print("Invalid character!")
            break


market(7)           # call the function 

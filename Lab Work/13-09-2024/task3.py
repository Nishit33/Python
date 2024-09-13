
# Travel Guide Project work in progress few days 

while True:

    Home=(input("Where You are : "))

    Where=input("Where You are going : ")

    travel="""

    1 Plane

    2 Train

    3 Bus

    4 Car
        
    """

    print(travel)

    choice=int(input("Enter Your choice how to go : "))

    if choice==1:
        print()
        print("Yeah You selected Plane")
        print()

        menu="""
        1 Business class
        2 Economy class
        """

        print(menu)
        print()

        ch=int(input("Enter Your Choice : "))

        if ch==1:
            print("Yeha you selected Business class")
            print()
            print("Welcome to business class!")


        Ticket=input("Please Select Ticket : ")



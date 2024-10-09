
# Inheritance 

class Myclass:
    
    def myfun1(self):

        n = input("Enter Name : ")
        n1 = n[::-1]

        if n==n1:
            print("Palindrome!!")

        else:
            print("Not Palindrome")    


class Myclass2:        

    def myfun1(self):

        l = [1,56,8,2,9]

        l.sort()

        print("Shortest : ",l[0])

        print("Largest : ",l[-1])


class Myclass3:

    def myfun1(self):

        d = {}

        n = int(input("Enter Number : "))

        for i in range(1,n+1):

            d[i]=i*i

        print(d)


obj = Myclass()


obj1 = Myclass2()


obj2 = Myclass3()



while True:

    menu = """

    press 1 for palindrome 
    press 2 for largest and smallest number 
    press 3 for square number 
    press 4 for exit 


    """
    print(menu)

    choice = int(input("Enter Your Choice : "))

    if choice==1:
        obj.myfun1()

    elif choice==2:
        obj1.myfun1()

    elif choice==3:
        obj2.myfun1()

    elif choice==4:
        print("Thank You !!!")    
        break

    else:
        print("Invalid choice")
        break




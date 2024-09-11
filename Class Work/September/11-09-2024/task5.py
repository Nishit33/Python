
from task4 import * # this is for import to another file to connect this file 

while True:
    menu = """

    press 1 for factorial 
    press 2 for Right angle 
    press 3 for left anngle
    press 4 for triangle
    press 5 for exit

    """

    print(menu)


    choice=int(input("Enter Your choice : "))

    if choice==1:
        n= int(input("Enter Number : "))
        myfun(n)

    elif choice==2:
        pattern1()

    elif choice==3:
        pattern2()    


    elif choice==4:
        pattern3()


    elif choice==5:
        print("Thank You")        
        break


    else:
        print("Invalid choice")   
        break






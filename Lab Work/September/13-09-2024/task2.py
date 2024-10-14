from Task1 import *


while True:

    menu="""

    press 1 for Addition 
    press 2 for Factorial 
    press 3 for Prime
    press 4 for Right angle pattern
    press 5 for Left angle pattern
    press 6 for Triangle Pattern
    press 7 for Exit!!


    """
    print(menu)

    choice=int(input("Enter Choice Number : "))
    print()

    if choice==1:
        add()

    elif choice==2:
        fact()    

    elif choice==3:
        prime()    

    elif choice==4:
        right()    

    elif choice==5:
        left()    
    
    elif choice==6:
        Triangle()    

    elif choice==7:
        print("Thank You!")        
        break

    else:
        print("Invalid Number !!")    
        break

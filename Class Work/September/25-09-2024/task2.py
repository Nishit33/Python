# Guess game
import random
a = random.randint(1,51)
while True:
    menu="""

    ********** Welcome To Game **********

    """

    print(menu)
    print()

    n=int(input("Enter Number : "))

    if n>=50:
        print("Number is invalid!!")

    elif n>a:
        print("Number is bigger than original!")    

    elif n<a:
        print("Number is smaller than original!!")    

    else:
        print("You win!!")
        break



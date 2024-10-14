# rock paper scissors 

import random


l=["Rock" , "Paper" , "Scissors"]

sum=0
sum1=0

for i in range(1,5):
    l1 = random.choice(l)

    print()
    print("*"*30,"Welcome to Game","*"*30)
    print()
    print("*"*30,f"Round {i} : ","*"*30)


    menu = """
                Press r for rock
                Press p for paper
                Press s for scissors
    """

    print(menu)

    uchoice = input("Enter Your Choice : ").lower()

    if uchoice=="r" or uchoice=="p" or uchoice=="s":


        if l1=="Rock" and uchoice=="p":
            print("User Win !!!")
            sum+=1
            print("Computer choice : ",l1)

        elif l1=="Paper" and uchoice=="s":
            print("User win !!")
            sum+=1
            print("Computer choice : ",l1)

        elif l1=="Scissors"  and uchoice=="r":
            print("User Win !!")  
            sum+=1
            print("Computer choice : ",l1)

        else:
            print("Computer Win!!")    
            sum1+=1
            print("Computer choice : ",l1)

    else:
        print("Invalid Choice!!")        


print()        

print("User win count : ",sum)
print("Computer win count : ",sum1)

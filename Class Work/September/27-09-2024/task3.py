# Rock  Paper  Scissors Game 

import random                       # import random number 

l = ["Rock" , "Paper" , "Scissors"]         # l = rock paper and scissors 

sum=0                                   # sum =0 

for i in range(1,5):                # for i in range (1,5)
    l1 = random.choice(l)           # l1 = random.choice(l)

    print()
    print("*"*30,"Welcome To The Game","*"*30)      # Print game heading 
    print()
    print("*"*30,f"Round {i} is started","*"*30)        # print round 1 to 4 
    print()

    menu ="""                              
            Press R for Rock
            Press P for Paper
            Press S for Scissors

    """

    print(menu)                         # print menu user asking which letter 

    uchoice = input("Enter Choice : ").lower()      # uchoice asking choice 
    if uchoice=="r" or uchoice=="p"  or uchoice=="s" :      # if choice r , p , s 


        if l1 =="Rock" and uchoice=="p":        # if l1 rock and choice== p that mean user win 
            print("User Win!!")
            sum+=100                             # and count 100 point user account 
            print("Computer Choice : ",l1)      # computer choice show 
            

        elif l1 =="Paper" and uchoice=="s":         # elif l1 paper and choice s that mean user win 
            print("User Win!!")
            sum+=100                             # and count 100 point user account 
            print("Computer Choice : ",l1)              # computer choice show
            

        elif l1 =="Scissors" and uchoice=="r":      # elif l1 Scissors and choice r that mean user win 
            print("User Win!!")
            sum+=100                                #count 100 point user account 
            print("Computer Choice : ",l1)              # computer choice show
            


        else:                                       # else sorry computer win and computer choice show 
            print("Sorry Computer Win!!!")
            print("Computer Choice : ",l1)    

    else:                                   # else input invalid choice 
        print("Invalid Choice!!")        

print()
print("Your Final Score is : ",sum)             # final score output user how much earn in this game 

        
        


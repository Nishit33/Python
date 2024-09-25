# sign-up page , Login page , forgot password 

import random
otp = random.randint(1001,9999)

d={}

while True:

    menu="""
    Press 1 for Sign-up
    Press 2 For Login
    Press 3 For Forgot-Password
    Press 4 For Exit
    """

    print(menu)

    choice=int(input("Enter Your choice : "))

    if choice==1:
        print("*"*50,"Welcome to sign-up page","*"*50)
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        mobile = int(input("Enter Mobile : "))
        password = int(input("Enter Password : "))
        cpassword = int(input("Enter Confirm password : "))

        if password==cpassword:
            d['name']=name
            d['email']=email
            d['mobile']=mobile
            d['password']=password
            print("Sign-up sucessfully!!")

        else:
            print("Invalid password")    


    elif choice==2:
        print("*"*50,"Welcome to Login page","*"*50)
        email = input("Enter Email : ")
        password = int(input("Enter Password : "))

        if d['email']==email and d['password']==password:
            print("Login Sucessfully!!")

        else:
            print("Invalid Credentials!!")    


    elif choice==3:
        print("*"*10,"Forgot Password","*"*10) 

        mobile = int(input("Enter Mobile Number : "))       
        
        if d['mobile']==mobile:
            print("*"*5,"OTP : ",otp,"*"*5)

            uotp = int(input("Enter OTP : "))


            if uotp==otp:
                password = int(input("Enter New password : "))

                d['password']=password

                print("Your New password sucessfully updated!!!")

            else:
                print("invalid otp!!")    


        else:
            print("Number is invalid!!!")
         

    elif choice==4:
        print("Thank You!!")
        break


    else:
        print("Invalid Choice!!")   
        break 



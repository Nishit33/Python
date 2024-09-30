
import random
otp = random.randint(1001,9999)

d={}

while True:
    menu="""
    press 1 for Signup
    press 2 for Login
    press 3 for Forgot-Password
    press 4 for Exit
    """
    print(menu)

    choice=int(input("Enter Your Choice : "))

    if choice==1:
        print("*"*25,"Welcome to signup page","*"*25)
        print()
        print()
        name=input("Enter Name : ")
        email=input("Enter Email : ")
        mobile=int(input("Enter Mobile Number : "))
        password=int(input("Enter Password : "))
        cpassword=int(input("Enter Confirm password : "))

        if password==cpassword:
            d['name']=name
            d['email']=email
            d['mobile']=mobile
            d['password']=password
            print("Sign-up Sucessfully !")

        else:
            print("Invalid Password!")

    elif choice==2:
        print("*"*25,"Welcome To Login Page","*"*25)     
        email=input("Enter Email : ")   
        password=int(input("Enter Password : "))

        if d['email']==email and d['password']==password:
            print("Login Succesfully")

        else:
            print("Invalid Email or password !!")    


    elif choice==3:
        print("*"*25,"Forgot Password","*"*25)

        mobile = int(input("Enter Mobile Number : "))

        if d['mobile']==mobile:
            print("*"*10,"OTP : ",otp,"*"*10)
            print()

            uotp=int(input("Enter OTP : "))

            if uotp==otp:
                password=int(input("Enter New Password : "))

                d['password']=password

                print("Your New password sucessfully updated!!")

            else:
                print("Invalid OTP !!!!")   

        else:
            print("Invalid Mobile Number!!")         


    elif choice==4:
        print("Thank You!")            
        break

    else:
        print("Invalid Choice Number Please input correct number !!")

                     

        


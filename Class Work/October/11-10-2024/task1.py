# Multi Level 

d ={}

class A:

    def register(self):

        name = input("Enter Your Name : ")
        roll_no = int(input("Enter Your Roll Number : "))

        d['name']=name
        d['roll_no']=roll_no

        print("Register sucessfully!!")


class B(A):
    maths = 80
    english = 75
    science = 69

    def authenticate(self):

        name=input("Enter Student Name : ")
        roll_no = int(input("Enter Roll Number : "))

        self.name=name
        self.roll_no=roll_no


        if d['name']==self.name  and d['roll_no']==self.roll_no :

            print("**************Your Result is as follow ******************")
            print("Marks of Maths : ",self.maths)
            print("Marks of English : ",self.english)
            print("Marks of Science : ",self.science)

        else:
            print("Invalid Credential !!")    

class C(B):

    def show(self):
        if d['name']==self.name  and d['roll_no']== self.roll_no :
            Total = self.maths+self.english+self.science
            print("Your Total is : ",Total)
            print("Percentage : ",Total/3)




obj = C()

menu="""
press 1 for Register 
press 2 fot exit

"""

print(menu)

choice= int(input("Enter Your choice : "))


if choice==1:
    obj.register()

    menu1 = """
    press 1 for Login
    press 2 for Exit 
    
    """

    print(menu1)

    choice1=int(input("Enter choice Number : "))

    if choice1==1:
        obj.authenticate()

        obj.show()

    else:
        print("Thank you !!")

else:
    print("Thankyou!! ")


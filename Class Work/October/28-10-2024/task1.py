from tkinter import * 
from tkinter import messagebox 
import pymysql
from login_3 import *

root = Tk()

def insert():
    name = ename.get()
    email = eemail.get()
    mobile = emobile.get()
    password = epassword.get()
    cpassword = ecpassword.get()


    if password == cpassword:
        db = pymysql.connect(host="localhost" , user="root" , password="" , database="Python")
        cursor = db.cursor()


        sql = "INSERT INTO cooper(NAME , EMAIL , MOBILE , password) VALUES('%s' , '%s' , '%s' , '%s' )"
        args = (name,email,mobile,password)
        cursor.execute(sql%args)
        db.commit()

        print("Data Inserted Successfully !!")
        messagebox.showinfo("Sucess" , "Data Inserted Succesfully")

        cursor.close()
        db.close()

    else:
        print("Both Passwords are not same!!")
        messagebox.showwarning("Incorrect Password" , "Both Password are not same")


root.geometry("500x500")
root.title("Signup Form")

name= Label(root,text="Name",font=("Calibri" , 20 , "bold"))
name.place(x=50 , y=50)

email= Label(root,text="Email",font=("Calibri" , 20 , "bold"))
email.place(x=50,y=100)

mobile= Label(root,text="Mobile",font=("Calibri" , 20 , "bold"))
mobile.place(x=50 , y=150)

password= Label(root,text="Password",font=("Calibri" , 20 , "bold"))
password.place(x=50 , y=200)

cpassword= Label(root,text="Confirm Password",font=("Calibri" , 20 , "bold"))
cpassword.place(x=50 , y=250)



ename= Entry(root,bg="lightblue")
ename.place(x=280 , y=60)

eemail= Entry(root,bg="lightblue")
eemail.place(x=280 , y=110)

emobile= Entry(root,bg="lightblue")
emobile.place(x=280 , y=160)

epassword= Entry(root,bg="lightblue",show="*")
epassword.place(x=280 , y=210)

ecpassword= Entry(root,bg="lightblue",show="*")
ecpassword.place(x=280 , y=260)

button = Button(root,text="Submit",bg="lightgreen",font=("calibri",20,"bold"),command=insert)
button.place(x=170 , y=320 ,height="40",width="100")


Login = Button(root,text="Login",bg="lightgreen",font=("calibri",20,"bold"),command=login1)
Login.place(x=280 , y=320 ,height="40",width="100")



root.mainloop()
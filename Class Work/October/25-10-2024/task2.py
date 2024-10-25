# Tkinter

from tkinter import * 

root = Tk()


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

epassword= Entry(root,bg="lightblue")
epassword.place(x=280 , y=210)

ecpassword= Entry(root,bg="lightblue")
ecpassword.place(x=280 , y=260)

Button = Button(root,text="Submit",bg="lightgreen",font=("calibri",20,"bold"))
Button.place(x=190 , y=320 ,height=40,width=100)


# root.config(bg="white")


root.mainloop()
from tkinter import * 




def login1():

    root = Tk()
    root.geometry("500x500")
    root.title("Login")

    email= Label(root,text="Email",font=("Calibri" , 20 , "bold"))
    email.place(x=50,y=100)

    password= Label(root,text="Password",font=("Calibri" , 20 , "bold"))
    password.place(x=50 , y=150)


    eemail= Entry(root,bg="lightblue")
    eemail.place(x=280 , y=110)


    epassword= Entry(root,bg="lightblue",show="*")
    epassword.place(x=280 , y=160)

    button1 = Button(root,text="Submit",bg="lightgreen",font=("calibri",20,"bold"),command=INSERT)
    button1.place(x=170 , y=320 ,height="40",width="100")
    
    
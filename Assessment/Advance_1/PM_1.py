# product management application 

from tkinter import *
from tkinter import messagebox
from dbase import *

class A:                    # First Page Two Option PM / Customer
    def __init__(self):
        # Initialize the main window
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Product Management System")
        
    def home(self):
        # Clear all widgets in the main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        details = Label(self.root, text="Product Management", fg="white", bg="orange", font=("Arial", 12, "bold"))
        details.pack(fill="x")

        # Product Manager Button
        Product = Button(self.root, text="Product Manager", fg="black", bg="white", font=("calibri", 14, "bold"), command=self.prod)  # Call prod method directly
        Product.place(x=130, y=110, height="40", width="250")

        # Customer Button
        Customer = Button(self.root, text="Customer", fg="black", bg="white", font=("calibri", 14, "bold"), command=self.cust)  # Call cust method directly
        Customer.place(x=130, y=180, height="40", width="250")

        self.root.mainloop()


class B(A):                     # Product Manager Page And Option
    def prod(self):
        # Hide the main window
        self.root.withdraw()

        # New window for Product Manager
        prod_window = Toplevel(self.root)
        prod_window.geometry("500x500")
        prod_window.title("Product Manager")

        details = Label(prod_window, text="Product Manager", fg="white", bg="orange", font=("Arial", 12, "bold"))
        details.pack(fill="x")

        # Register button
        Register1 = Button(prod_window, text="Register", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.reg)
        Register1.place(x=130, y=110, height="40", width="250")

        # Login button
        Login1 = Button(prod_window, text="Login", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.log)
        Login1.place(x=130, y=180, height="40", width="250")

        # Manage Products button
        Manage1 = Button(prod_window, text="Manage All Product Stocks", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.man)
        Manage1.place(x=130, y=260, height="40", width="250")

        # View Stocks button
        view1 = Button(prod_window, text="View All Stocks", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.ve)
        view1.place(x=130, y=340, height="40", width="250")

        # Back button
        back_button = Button(prod_window, text="🔙", font=("Arial", 14), command=lambda: self.go_back(prod_window))
        back_button.place(x=20, y=30, height=30, width=40)

    def go_back(self, current_window):
        # Close the current window and show the main window again
        current_window.destroy()
        self.root.deiconify()


class C(B):                             # Customer Page And Option
    def cust(self):
        # Hide the main window
        self.root.withdraw()

        # New window for Customer
        cust_window = Toplevel(self.root)
        cust_window.geometry("500x500")
        cust_window.title("Customer")

        details = Label(cust_window, text="Customer Page", fg="white", bg="orange", font=("Arial", 12, "bold"))
        details.pack(fill="x")

        # Register button
        Register2 = Button(cust_window, text="Register", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.creg)
        Register2.place(x=130, y=110, height="40", width="250")

        # Login button
        Login2 = Button(cust_window, text="Login", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.Clog)
        Login2.place(x=130, y=180, height="40", width="250")

        # Purchase Stocks button
        Manage2 = Button(cust_window, text="Purchase Stocks", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.Cpur)
        Manage2.place(x=130, y=260, height="40", width="250")

        # View Orders button
        view2 = Button(cust_window, text="View All Orders", fg="black", bg="white", font=("calibri", 14, "bold"),command=self.viewC)
        view2.place(x=130, y=340, height="40", width="250")

        # Back button
        back_button = Button(cust_window, text="🔙", font=("Arial", 14), command=lambda: self.go_back(cust_window))
        back_button.place(x=20, y=30, height=30, width=40)



class D(C):                         # Product Manager Register
 
    def reg(self):
        self.root.withdraw()

        def validate_form():

        # Check if any required field is empty
            if not ename.get() or not econtact.get() or not eemail.get() or not gender_var.get() or not estate.get() or not ecity.get():
                messagebox.showwarning("Warning", "Fill the empty field !!")  # Show warning message
            else:
                sql = "SELECT * FROM product_manager where email = '%s'"
                args = (eemail.get())
                cursor.execute(sql%args)
                data = cursor.fetchone()
                if data:
                    messagebox.showinfo("Ragister", f"{eemail.get()} is already register!!!!")
                else:
                    sql = "INSERT INTO product_manager(Name, email, Contact, Gender, State, City) VALUES('%s','%s','%s','%s','%s','%s')"
                    args = (ename.get(), eemail.get(), econtact.get(), gender_var.get(), estate.get(), ecity.get())
                    cursor.execute(sql%args)
                    db.commit()
                    messagebox.showinfo("Success", "Registration Successful!")


        reg_window = Toplevel(self.root)
        reg_window.geometry("480x510")
        reg_window.title("Registration Form")


        details = Label(reg_window,text="Please enter details below ",fg="white",bg="orange",font=("Arial" ,12 ,"bold"))
        details.pack(fill="x")




        name = Label(reg_window,text="Name *",font=("arial" ,12))
        name.place(x=20 , y=50)

        ename= Entry(reg_window,bg="White")
        ename.place(x=120,y=55,height=25,width=170)



        contact = Label(reg_window,text="Contact *",font=("arial",12))
        contact.place(x=20,y=100)

        econtact= Entry(reg_window,bg="White")
        econtact.place(x=120,y=100,height=25,width=170)


        email = Label(reg_window,text="Email *",font=("arial",12))
        email.place(x=20,y=150)

        eemail= Entry(reg_window,bg="White")
        eemail.place(x=120,y=148,height=25,width=170)


        gender = Label(reg_window,text="Gender *",font=("arial",12))
        gender.place(x=20,y=200)

        gender_var = StringVar()
        Radiobutton(reg_window, text="Male", variable=gender_var, value="Male", font=("Arial", 10 , "bold")).place(x=120, y=200)
        Radiobutton(reg_window, text="Female", variable=gender_var, value="Female", font=("Arial", 10, "bold")).place(x=200, y=200)


        state = Label(reg_window,text="State *",font=("arial" ,12))
        state.place(x=20,y=260)

        estate= Entry(reg_window,bg="White")
        estate.place(x=120,y=260,height=25,width=170)


        city = Label(reg_window,text="City *",font=("arial" ,12))
        city.place(x=20,y=320)

        ecity= Entry(reg_window,bg="White")
        ecity.place(x=120,y=320,height=25,width=170)



        button = Button(reg_window,text="Register",bg="orange",font=("arial" , 12 ,"bold"), command=validate_form)
        button.place(x=120,y=400,height=35,width=120)




class E(D):                     # Product Manager Login Page 

    def log(self):

        self.root.withdraw()
        def validate_form():

            if not eemail.get():
                messagebox.showwarning("Warning", "Fill the empty field !!")  # Show warning message
            else:
                sql = "SELECT * FROM product_manager WHERE email = '%s'"
                args = (eemail.get())
                cursor.execute(sql%args)
                data = cursor.fetchone()
                if data:
                    messagebox.showinfo("Success", "Login Successful!")
                else:
                    messagebox.showerror("Register", f"{eemail.get()} not registered..!!!!")

        log_window = Toplevel(self.root)
        log_window.geometry("480x510")
        log_window.title("Login")
        

        details = Label(log_window,text="Please enter details below ",fg="white",bg="orange",font=("Arial" ,12 ,"bold"))
        details.pack(fill="x")


        email = Label(log_window,text="Email *",font=("arial",12,"bold"))
        email.place(x=20,y=120)

        eemail= Entry(log_window,bg="White")
        eemail.place(x=120,y=120,height=25,width=170)


        button = Button(log_window,text="Login",bg="orange",font=("arial" , 12 ,"bold") , command=validate_form)
        button.place(x=120,y=200,height=35,width=120)


class F(E):                     # Product Manager         Manage All Product Stocks
    def __init__(self):
        super().__init__()
        self.product_data = []  # Shared storage for product data

    def man(self):
        self.root.withdraw()

        # Set up the main window
        man_window = Toplevel(self.root)
        man_window.title("Manage Product Stocks")
        man_window.geometry("500x500")

        # UI components
        details = Label(man_window, text=" ", fg="white", bg="orange", font=("Arial", 12, "bold"))
        details.pack(fill="x")

        produ = Label(man_window, text="Fruit Name *", font=("arial", 12))
        produ.place(x=20, y=50)

        eprodu = Entry(man_window, bg="White", font=(12))
        eprodu.place(x=150, y=50, height=25, width=170)

        qun = Label(man_window, text="Quantity *", font=("arial", 12))
        qun.place(x=20, y=100)

        equn = Entry(man_window, bg="White", font=(12))
        equn.place(x=150, y=100, height=25, width=170)

        price = Label(man_window, text="Price *", font=("arial", 12))
        price.place(x=20, y=150)

        eprice = Entry(man_window, bg="White", font=(12))
        eprice.place(x=150, y=150, height=25, width=170)

        def clear_fields():
            eprodu.delete(0, END)
            equn.delete(0, END)
            eprice.delete(0, END)

        def add_stock():
            if not eprodu.get() or not equn.get() or not eprice.get():
                messagebox.showerror("Error", "Please Add Data")
            else:
                self.product_data.append((eprodu.get(), equn.get(), eprice.get()))  # Save product data

                stock_info.config(state="normal")
                stock_info.insert(END, f"Fruit: {eprodu.get()}, Quantity: {equn.get()}, Price: {eprice.get()}\n")
                stock_info.config(state="disabled")
                messagebox.showinfo("Success", "Fruit Registered Successfully!")
                clear_fields()

        # Add buttons
        clear_button = Button(man_window, text="Clear All", bg="red", fg="white", font=("arial", 12, "bold"), command=clear_fields)
        clear_button.place(x=70, y=200, height=35, width=120)

        button = Button(man_window, text="Add Stock", bg="lightgreen", font=("arial", 12, "bold"), command=add_stock)
        button.place(x=200, y=200, height=35, width=120)

        stock_info = Text(man_window, height=10, width=60)
        stock_info.place(x=20, y=250)
        stock_info.insert(END, "Added Stock Details:\n")  # Title line in text area
        stock_info.config(state="disabled")  # Make the text area initially read-only


    

class G(F):                             # Product Manager    View All Stocks
    def ve(self):
        ve_window = Toplevel(self.root)
        ve_window.title("View All Stock")
        ve_window.geometry("500x500")

        # Retrieve and display product data
        if self.product_data:
            for index, (name, quantity, price) in enumerate(self.product_data, start=1):
                Label(ve_window, text=f"{index}. {name} - Qty: {quantity} - Price: {price}").pack(anchor="w", padx=10, pady=5)
        else:
            Label(ve_window, text="No stock data available.", font=("Arial", 12, "italic")).pack(pady=20)

        ve_window.mainloop()



class H(G):                         # Customer    Register Page 

    def creg(self):
        self.root.withdraw()

        def validate_form():

            # Check if any required field is empty
            if not Cename.get() or not Cecontact.get() or not Ceemail.get() or not Cgender_var.get() or not Cestate.get() or not Cecity.get():
                messagebox.showwarning("Warning", "Fill the empty field !!")  # Show warning message
            else:
                sql = "SELECT * FROM customer where email = '%s'"
                args = (Ceemail.get())
                cursor.execute(sql%args)
                data = cursor.fetchone()
                if data:
                    messagebox.showinfo("Ragister", f"{Ceemail.get()} is already register!!!!")
                else:
                    sql = "INSERT INTO customer(Name, email, Contact, Gender, State, City) VALUES('%s','%s','%s','%s','%s','%s')"
                    args = (Cename.get(), Ceemail.get(), Cecontact.get(), Cgender_var.get(), Cestate.get(), Cecity.get())
                    cursor.execute(sql%args)
                    db.commit()
                    messagebox.showinfo("Success", "Registration Successful!")




        creg_window = Toplevel(self.root)

        creg_window.geometry("480x510")
        creg_window.title("Registration Form")


        Cdetails = Label(creg_window,text="Please enter details below ",fg="white",bg="orange",font=("Arial" ,12 ,"bold"))
        Cdetails.pack(fill="x")


        Cname = Label(creg_window,text="Name *",font=("arial" ,12))
        Cname.place(x=20 , y=50)

        Cename= Entry(creg_window,bg="White")
        Cename.place(x=120,y=55,height=25,width=170)


        Ccontact = Label(creg_window,text="Contact *",font=("arial",12))
        Ccontact.place(x=20,y=100)

        Cecontact= Entry(creg_window,bg="White")
        Cecontact.place(x=120,y=100,height=25,width=170)



        Cemail = Label(creg_window,text="Email *",font=("arial",12))
        Cemail.place(x=20,y=150)

        Ceemail= Entry(creg_window,bg="White")
        Ceemail.place(x=120,y=148,height=25,width=170)



        Cgender = Label(creg_window,text="Gender *",font=("arial",12))
        Cgender.place(x=20,y=200)

        Cgender_var = StringVar()
        Radiobutton(creg_window, text="Male", variable=Cgender_var, value="Male", font=("Arial", 10 , "bold")).place(x=120, y=200)
        Radiobutton(creg_window, text="Female", variable=Cgender_var, value="Female", font=("Arial", 10, "bold")).place(x=200, y=200)



        Cstate = Label(creg_window,text="State *",font=("arial" ,12))
        Cstate.place(x=20,y=260)

        Cestate= Entry(creg_window,bg="White")
        Cestate.place(x=120,y=260,height=25,width=170)



        Ccity = Label(creg_window,text="City *",font=("arial" ,12))
        Ccity.place(x=20,y=320)

        Cecity= Entry(creg_window,bg="White")
        Cecity.place(x=120,y=320,height=25,width=170)


        Cbutton = Button(creg_window,text="Register",bg="orange",font=("arial" , 12 ,"bold"), command=validate_form)
        Cbutton.place(x=120,y=400,height=35,width=120)



class I(H):                     # Customer Login Page 

    def Clog(self):

        self.root.withdraw()

        def validate_form():
            if not Ceemail.get():
                messagebox.showwarning("Warning", "Fill the empty field !!")  # Show warning message
            else:
                sql = "SELECT * FROM customer WHERE email = '%s'"
                args = (Ceemail.get())
                cursor.execute(sql%args)
                data = cursor.fetchone()
                if data:
                    messagebox.showinfo("Success", "Login Successful!")
                else:
                    messagebox.showerror("Register", f"{Ceemail.get()} not registered..!!!!")

        

        clog_window = Toplevel(self.root)
        clog_window.geometry("480x510")
        clog_window.title("Login")


        Cdetails = Label(clog_window,text="Please enter details below ",fg="white",bg="orange",font=("Arial" ,12 ,"bold"))
        Cdetails.pack(fill="x")


        Cemail = Label(clog_window,text="Email *",font=("arial",12,"bold"))
        Cemail.place(x=20,y=120)

        Ceemail= Entry(clog_window,bg="White")
        Ceemail.place(x=120,y=120,height=25,width=170)


        Cbutton = Button(clog_window,text="Login",bg="orange",font=("arial" , 12 ,"bold") , command=validate_form)
        Cbutton.place(x=120,y=200,height=35,width=120)



            
class J(I):                             # Customer Purchase Stocks Page 

    def Cpur(self):
        self.root.withdraw()

        # Set up the main window
        cpur_window = Toplevel(self.root)
        cpur_window.title("Purchase Stock")
        cpur_window.geometry("500x500")


        Cdetails = Label(cpur_window,text=" ",fg="white",bg="orange",font=("Arial" ,12 ,"bold"))
        Cdetails.pack(fill="x")


        Cprodu = Label(cpur_window,text="Fruit Name *",font=("arial" ,12))
        Cprodu.place(x=20 , y=50)

        Ceprodu= Entry(cpur_window,bg="White",font=(12))
        Ceprodu.place(x=150,y=50,height=25,width=170)



        Cqun = Label(cpur_window,text="Quantity *",font=("arial" ,12))
        Cqun.place(x=20 , y=100)

        Cequn= Entry(cpur_window,bg="White",font=(12))
        Cequn.place(x=150,y=100,height=25,width=170)



        Cprice = Label(cpur_window,text="Price *",font=("arial" ,12))
        Cprice.place(x=20 , y=150)

        Ceprice= Entry(cpur_window,bg="White",font=(12))
        Ceprice.place(x=150,y=150,height=25,width=170)


        def clear_fields():
            Ceprodu.delete(0, END)
            Cequn.delete(0, END)
            Ceprice.delete(0, END)


        def add_stcok():
            if not Ceprodu.get() or not Cequn.get() or not Ceprice.get() :
                messagebox.showerror("Error","Please Add Data")

            else:
                with open("customer_orders.txt", "a") as f:
                    f.write(f"Fruit: {Ceprodu.get()}, Quantity: {Cequn.get()}, Price: {Ceprice.get()}\n")
                    stock_info.config(state="normal")
                    stock_info.insert(END, f"Fruit: {Ceprodu.get()}, Quantity: {Cequn.get()}, Price: {Ceprice.get()}\n")
                    stock_info.config(state="disabled")
                    messagebox.showinfo("Success", "Fruit Buy Successfully!")
                    clear_fields()
            

        # Add buttons
        clear_button = Button(cpur_window, text="Cancel", bg="red", fg="white", font=("arial", 12, "bold"), command=clear_fields)
        clear_button.place(x=70, y=200, height=35, width=120)


        Cbutton = Button(cpur_window,text="Buy Stock",bg="lightgreen",font=("arial" , 12 ,"bold"),command=add_stcok)
        Cbutton.place(x=200,y=200,height=35,width=120)

        stock_info = Text(cpur_window, height=10, width=60)
        stock_info.place(x=20, y=250)
        stock_info.insert(END, "Added Stock Details:\n")  # Title line in text area
        stock_info.config(state="disabled")  # Make the text area initially read-only



class K(J):                             # Customer View Page 

    def viewC(self):
        self.root.withdraw()


        viewC = Toplevel(self.root)
        viewC.title("View All Orders")
        viewC.geometry("500x500")

        orders_info = Text(viewC, height=20, width=60)
        orders_info.pack()
        orders_info.insert(END, "All Customer Orders:\n")
        
        try:
            with open("customer_orders.txt", "r") as f:
                orders_info.insert(END, f.read())
        except FileNotFoundError:
            orders_info.insert(END, "No orders found.")

        orders_info.config(state="disabled")
        viewC.mainloop()

        




# Create an instance of C and start with the home page
if __name__ == "__main__":
    app = K()
    app.home()

from task1 import *

mydb = pymysql.connect(host="localhost",user="root",password="",database="nishit18")
mycursor = mydb.cursor()

while True:
    menu="""

    press 1 for Insert Data
    press 2 for Update Data
    press 3 for Delete Data
    press 4 for Fetch Data
    press 5 for Exit 

    """
    print(menu)

    choice = int(input("Enter Your choice : "))

    if choice==1:
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        password = int(input("Enter Password : "))

        query = "insert into flipkart (name,email,password) values ('%s' , '%s' , '%s' )"
        args = (name,email,password)
        mycursor.execute(query%args)
        mydb.commit()
        print("Data Inserted Sucessfully!!")

    elif choice==2:
        id = int(input("Enter Id : "))    
        name = input("Enter Name for update : ")
        email = input("Enter Email for update : ")
        password = int(input("Enter Password for update : "))

        query = "update flipkart set name='%s' , email='%s' , password='%s' where id = '%s'"
        args = (name,email,password,id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Data Updated!!")

    elif choice==3:
        id = int(input("Enter Id : "))    

        query = "delete from flipkart where id = '%s' "
        args=(id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Data Deleted!!")


    elif choice==4:
        query = "select * from flipkart"    
        mycursor.execute(query)
        data = mycursor.fetchall()
        print(data)


    elif choice==5:
        print("Thankyou!!")
        break

    else:
        print("Invalid Choice!!")
        break
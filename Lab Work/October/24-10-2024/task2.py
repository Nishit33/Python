from task1 import *

mydb = pymysql.connect(host="localhost" , user="root" , password="" , database="Sports")
mycursor = mydb.cursor()

while True:

    menu = """

    press 1 for Insert Data
    press 2 for Update Data
    press 3 for Delete Data
    press 4 for Fetch Data
    press 5 for Exit


    """
    print(menu)

    choice = int(input("Enter Your Choice : "))

    if choice==1:

        Name = input("Enter Your Name : ")
        Number = int(input("Enter Your Jersey Number : "))
        State = input("Enter Your State : ")

        query = "insert into cricket (name,number,state) values ('%s' , '%s' , '%s')"
        args = (Name,Number,State)
        mycursor.execute(query%args)
        mydb.commit()
        print()
        print("Data Inserted Sucessfully!!")


    elif choice==2:

        id = int(input("Enter Your Id : "))   
        Name = input("Enter Your Name : ")
        Number = int(input("Enter Your Jersey Number : "))
        State = input("Enter Your State : ")

        query = "update cricket set name='%s' , number='%s' , state='%s' where id = '%s'"
        args=(Name,Number,State,id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Data Updated Sucessfully !!")



    elif choice==3:

        id = int(input("Enter Id : "))

        query = "delete from cricket where id = '%s' "
        args=(id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Data Deleted Sucessfully !!")


    elif choice==4:

        query = "select * from cricket"
        mycursor.execute(query)
        data = mycursor.fetchall()
        print()
        print(data)


    elif choice==5:

        print("Thank You !!")
        break


    else:

        print("Invalid Choice !!!")
        break


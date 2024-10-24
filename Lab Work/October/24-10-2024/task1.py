import pymysql

mydb = pymysql.connect(host="localhost" , user="root" , password="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists Sports")
mydb.commit()

mydb = pymysql.connect(host="localhost" , user="root" , password="" , database="Sports")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists cricket (Id int primary key auto_increment , Name varchar (30) , Number int  , State varchar (30) ) ")
mydb.commit()
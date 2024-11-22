import pymysql

db = pymysql.connect(host="localhost" , user="root" , password="")
cursor = db.cursor()

cursor.execute("create database if not exists product_management")
db.commit()

db = pymysql.connect(host="localhost" , user="root" , password="" , database="product_management")
cursor = db.cursor()

cursor.execute("create table if not exists product_manager(manager_id int primary key auto_increment not null, Name varchar(25), email varchar(25) unique, Contact bigint unique, Gender varchar(25), State varchar(25), City varchar(25))")
db.commit()

cursor.execute("create table if not exists customer(customer_id int primary key auto_increment not null, Name varchar(25), email varchar(25) unique, Contact bigint unique, Gender varchar(25), State varchar(25), City varchar(25))")
db.commit()



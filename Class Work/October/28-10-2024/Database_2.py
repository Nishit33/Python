import pymysql

db = pymysql.connect(host="localhost" , user="root" , password="")
cursor = db.cursor()

cursor.execute("Create Database if not exists python")
db.commit()

db = pymysql.connect(host="localhost" , user="root" , password="" , database="python")
cursor = db.cursor()

cursor.execute("Create Table if not exists Cooper(ID INT PRIMARY KEY AUTO_INCREMENT , NAME VARCHAR (30) , EMAIL VARCHAR (30) ,password varchar(30) , MOBILE BIGINT )")
db.commit()
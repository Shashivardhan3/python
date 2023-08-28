#Create a database(mydb17) within mysql

import pymysql

#Creating the connection object
con=pymysql.connect(host="localhost",user="root",password="root") #con ----->connection object

#Creating cursor object
cur1=con.cursor()  #cur1---->cursor object

cur1.execute("create database mydb17")
print("DATABASE CREATED SUCCESSFULLY!!!!")

cur1.close()

con.close()

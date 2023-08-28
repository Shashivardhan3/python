#Creating a table,inserting data and Retrieving data
#create a student table

import pymysql

#Creating connection object
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb17")#con-->connection object

#Creating a cursor object
cur1=con.cursor()
#cur1.execute("create table student(rollno int,name varchar(10),marks int)")
#print("TABLE CREATED SUCESSFULLY!!!")
#inserting data
cur1.execute("insert into student values(501,'Ajay',90),(502,'Rahul',75),(503,'James',60)")
print("DATA INSERTED SUCCESSFULLY!!!")
con.commit()
#Retrieving the data
cur1.execute("select * from student")
#The o/p rows or records of the sql query are stored within the cur1 object

#Retrieving one by one row using for loop

for row in cur1:
    print(row)
    
cur1.close()
con.close()

#------------------------------------------------------------------------
#o/p:

#Goto Mysql and check

mysql> use mydb17;
Database changed
mysql> show tables;
+------------------+
| Tables_in_mydb17 |
+------------------+
| student          |
+------------------+
1 row in set (0.01 sec)

mysql> select * from student;
Empty set (0.00 sec)

mysql> select * from student;
+--------+-------+-------+
| rollno | name  | marks |
+--------+-------+-------+
|    501 | Ajay  |    90 |
|    502 | Rahul |    75 |
|    503 | James |    60 |
------------------------

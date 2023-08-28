#Creating a table from another table

import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb17")

#Creating cur1 object for creating a table
cur1=con.cursor()

cur1.execute("create table emp2 like emp")

#Inserting data from one table to another table
cur1.execute("insert into emp2 select * from mydb16.emp")
con.commit()

cur1.execute("select * from emp2")

for row in cur1:
    print(row)

cur1.close()
con.close()

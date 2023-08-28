#Creating multiple cursor objects
#cur1------>for creating a table
#cur2------>for inserting the data
#cur3------>for retrieving the data

#Creating emp table
import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb17")

#Creating cur1 object for creating a table
cur1=con.cursor()
cur1.execute("create table emp(eid int,ename varchar(20),sal int,sex varchar(1),dno int,city varchar(10))")
print("TABLE CREATED SUCCESSFULLY!!!")

#Create cur2 object for inserting data
cur2=con.cursor()
cur2.execute("insert into emp values(101,'Miller',10000,'m',11,'hyd'),(102,'Blake',20000,'m',12,'pune'),(103,'Sony',30000,'f',11,'pune'),(104,'Sita',40000,'f',12,'hyd'),(105,'James',50000,'m',13,'pune')")
con.commit() #for permanently saving
print("DATA INSERTED SUCCESSFULLY!!!")

#Create cur3 object for retrieving the data
cur3=con.cursor()
cur3.execute("select * from emp") #The o/p rows of this query are stored in cur3 object

for row in cur3:
    print(row)

cur3.close()
cur2.close()
cur1.close()

con.close()

#Note: we can perform all the above operations using single cursor object also
#why multiple cursor objects are required?
'''
cur1.execute("select * from emp") ---->here emp rows are stored in cur1 object

cur1.execute("select * from student")

for p in cur1:
    print(p)   -------->here we get only student records

but to retrieve both emp and student records

create 2 cursor objects for emp and student

cur1.execute("select * from emp") 

cur2.execute("select * from student") '''











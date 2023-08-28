
#Filtering the data using where clause
import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb17")

#Creating cur1 object for creating a table
cur1=con.cursor()

#i)Filter only those emps who belongs to the city "hyderabad"

cur1.execute("select * from emp where city='hyd'")
for row in cur1:
    print(row)
print("\n")
#---------------------------------------------------------------------------------
#ii) Filter only male emp records
cur1.execute("select * from emp where sex='m'")
for row in cur1:
    print(row)
print("\n")
#---------------------------------------------------------------------------------
#iii)Filter those emps whose sal>25000 and belongs to dno12
cur1.execute("select * from emp where sal>25000 and dno=12")
for row in cur1:
    print(row)

cur1.close()
con.close()

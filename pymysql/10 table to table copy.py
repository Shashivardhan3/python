#CTAS ---->CREATE-TABLE-AS-SELECT
#Table to table copy

import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb17")

#Creating cur1 object for creating a table
cur1=con.cursor()

cur1.execute("create table emp3 as select * from emp")

cur1.execute("select * from emp3")

for row in cur1:
    print(row)

cur1.close()
con.close()

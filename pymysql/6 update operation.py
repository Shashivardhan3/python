#update
import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb17")

#Creating cur1 object for creating a table
cur1=con.cursor()
cur1.execute("update emp set sal=sal+7000 where ename='Blake'")
con.commit()

cur1.execute("select * from emp")
for row in cur1:
    print(row)

cur1.close()
con.close()

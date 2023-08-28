#Python Database Connectivity(PDBC):

Python to connect with any database,we require a module

Python to connect with mysql database----->requires-------->pymysql (or)mysql.connector

Python to connect with Oracle database---->requires-------->cx_Oracle

Python to connect with sqlserver ------->requires---------->pyodbc

#Installing External modules:

The modules which are not part of Python software,we call them as external modules

These external modules we need to download and install by using a component called pip

pip: Pip is a Application or a package manager which quickly downloads or installs
      any external module,which is not part of Python software.

#where this pip is available??
pip is available within the installed folder of python--->C:\python310\scripts\pip

#Installing Pymysql module:

Goto command prompt:

C:\Users\DELL>cd\

C:\>cd python310

C:\Python310>cd scripts

C:\Python310\Scripts>pip uninstall pymysql

C:\Python310\Scripts>pip install pymysql

#python to connect with database and to perform any sql operations, we require 2 objects
1.connection object
2.cursor object

1.Connection object: If we call connect() function by providing the following connecting
                     parameters then the connection object is created

1)Hostname
2)username
3)password
4)Databasename
ex:
con=pymysql.conneect(host="localhost",user="root",password="root",database="mydb16")
here con is the connection object

2.cursor object: on the connection object, if i pass cursor method, then cursor object is
                 created

cur1=con.cursor()
here cur1 is the cursor object

within the cursor object,we have execute method,within which we can specify any valid sql query

cur1.execute("sql query")

The o/p of the sql query is stored within the cur1 object

we can retrieve one by one record or row by using for loop













    
















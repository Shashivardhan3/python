
#SQL operations:

mysql> show databases;

displays all the available databases

mysql> create database mydb16;

mysql> show databases;

#CRUD Operations:
C-CREATE
R-READ
U-UPDATE
D-DELETE

mysql> use mydb16;
Database changed

mysql> show tables;
Empty set (0.01 sec)

#1)Creating a emp table
mysql> create table emp(eid int,ename varchar(20),sal int,sex varchar(1),dno int,
       city varchar(10));

#2)Inserting data into the table
mysql> insert into emp values(101,'Miller',10000,'m',11,'hyd'),(102,'Blake',20000,'m',12,'pune'),
(103,'Sony',30000,'f',11,'pune'),(104,'Sita',40000,'f',12,'hyd'),(105,'James',50000,'m',13,'pune');

#3)Reading or Retrieving data from the database

#i)retrieving all the columns
mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 20000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | pune |
+------+--------+-------+------+------+------+

#ii)retrieving only the selected columns

mysql> select ename,sal from emp;
+--------+-------+
| ename  | sal   |
+--------+-------+
| Miller | 10000 |
| Blake  | 20000 |
| Sony   | 30000 |
| Sita   | 40000 |
| James  | 50000 |
+--------+-------+

#4) update:
mysql> update emp set sal=sal+5000 where ename="Blake";

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | pune |
+------+--------+-------+------+------+------+

#5)delete:

mysql> delete from emp where ename="James";

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+
#---------------------------------------------------------------------------------------------
#6) creating a table from another table

mysql> create table emp2 like emp;   #here we get only the table structure but not the data


mysql> select * from emp2;

mysql> describe emp2;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| eid   | int         | YES  |     | NULL    |       |
| ename | varchar(20) | YES  |     | NULL    |       |
| sal   | int         | YES  |     | NULL    |       |
| sex   | varchar(1)  | YES  |     | NULL    |       |
| dno   | int         | YES  |     | NULL    |       |
| city  | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+

#inserting data from one table to another table
#inserting data from emp to emp2

mysql> insert into emp2 select * from emp;


mysql> select * from emp2;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#7) Table to table copy:
#CTAS :CREATE -TABLE -AS -SELECT

mysql> create table emp3 as select * from emp;

mysql> select * from emp3;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+






















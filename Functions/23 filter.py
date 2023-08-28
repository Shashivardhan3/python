#filter(): for filtering operations
'''
filter() function takes 2 arguments:
    1.lambda function
    2.Iterable type like list
'''

#ex: 1
list1=[10,20,30,40,50,60]

#Task: Extract only those elements whose value >30
res1=list(filter(lambda x:x>30,list1))  #here x is each element of the list of type-->int
print(res1,type(res1))

#ex:2
emps=[[101,"miller",10000,'m',11,'hyd'],
      [102,"blake",20000,'m',12,'pune'],
      [103,'sony',30000,'f',11,'pune'],
      [104,'sita',40000,'f',12,'hyd'],
      [105,'john',50000,'m',13,'hyd']]

#Task 1: Filter only those emps who belongs to the city "hyd"
hyd_recs=list(filter(lambda x:x[5]=='hyd',emps))  #here x is each element which is of list type

print(hyd_recs)
print("\n")

#Task 2: Filter only male emp records
male_recs=list(filter(lambda x:x[3]=='m',emps))
print(male_recs)
print("\n")

#Task 3: Filter those emps who belongs to dno=12 and salary>20000
res2=list(filter(lambda x:x[4]==12 and x[2]>20000,emps))
print(res2)














    

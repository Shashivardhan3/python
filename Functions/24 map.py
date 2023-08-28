#map(): for each element transformation

#whatever transformation we apply, gets applied to each and every element
'''
map() function takes 2 arguments:
    1.lambda function
    2.Iterable type like list
'''

list1=[10,20,30,40,50]

#Task: adding 5 to each element of the list
res1=list(map(lambda x:x+5,list1))
print(res1)

#ex:2
emps=[[101,"miller",10000,'m',11,'hyd'],
      [102,"blake",20000,'m',12,'pune'],
      [103,'sony',30000,'f',11,'pune'],
      [104,'sita',40000,'f',12,'hyd'],
      [105,'john',50000,'m',13,'hyd']]

#Task 1: Adding 5000 to the sals of each employee as bonus
res2=list(map(lambda x:[x[0],x[1],x[2]+5000,x[3],x[4],x[5]],emps))
print(res2)
print("\n")

#Task2 : Transform each empname to start with uppercase
res3=list(map(lambda x:[x[0],x[1].capitalize(),x[2],x[3],x[4],x[5]],res2))
print(res3)
print("\n")

#Task3: Transform------>"m" ------>"male"
#                       "f" ------>"female"

res4=list(map(lambda x:[x[0],x[1],x[2],"male" if(x[3]=='m') else "female",x[4],x[5]],res3))
print(res4)


















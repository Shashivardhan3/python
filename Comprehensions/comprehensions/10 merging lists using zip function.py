
#merging 2 lists using zip() function
#Converting a list to dictionary

emps=["Ajay","Rahul","Amar","Ajith","James"]

sals=[10000,20000,30000,40000,50000]

#Now merging these 2 lists using zip() function

x=zip(emps,sals)
print(x,type(x))

y=list(x)
print(y,type(y))

z=dict(y)
print(z,type(z))

'''
w=dict(x)       
print(w,type(w)) 

for p in x:
    print(p)
   
w=dict(x)
print(w,type(w))  '''   

#Zip object gets exhausted(becomes empty) once an operation is performed on it,
#we cannot perform the 2nd operation


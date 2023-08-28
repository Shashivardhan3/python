#Categories of Function:

#1.Function without arguments and without returntype

def add1():         #No arguments
    x=10
    y=20
    z=x+y
    print("sum=",z) #No returntype
add1()

#---------------------------------------------------------------------------------------------
#2.Functions with arguments and without return type

def add2(x,y):       #with arguments
    z=x+y
    print("sum=",z)  #No returntype

add2(20,40)

print(add2(30,20)) #here nothing is stored within the function call

#---------------------------------------------------------------------------------------------
#3. Functions with arguments and with return type
#Note: Functions can also be used for assignments

def add3(x,y):
    z=x+y
    return z

print(add3(20,50)) #whatever the function returns is stored within the function call

p=add3(10,40)
print("p=",p)
#Note: The return stmt returns the computed results of a function and that can be used in the
#      later part of the program
#ex:
#Computing the netsalary with tax of 10%

salary=int(input("Enter the Salary:"))

def compute():
    tax=salary*(10/100)
    return tax
t=compute()
netsal=salary-t
print("NET SALARY=",netsal)
#----------------------------------------------------------------------------------------------
#Q) can a function return multiple values------>YES

def evaluate(s1,s2,s3):
    tot=s1+s2+s3
    avg=tot/3
    return tot,avg

x=evaluate(90,80,70)
print(x,type(x))
print("TOTAL=",x[0])
print("AVERAGE=",x[1])
#(or)

m,n=evaluate(60,70,80)
print("Total=",m)
print("Average=",n)

#---------------------------------------------------------------------------------------------
#4.Functions without arguments and with returntype

def add4():
    x=10
    y=20
    z=x+y
    return z
p=add4()
print("p=",p)






























    

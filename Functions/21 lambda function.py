'''
#Types of Functions:
1.Lambda Function (or) Anonymous function
2.Filter function
3.map function
4.reduce function
5.Boolean function
6.Recursive function '''

#Lambda function:

#A Function without anyname is called as lambda function.

#Syntax for defining a lambda function:
#lambda arguments : expression

#Q)If the function doesnt have anyname then how to call that function?

#Assign that function to a variable and the variable behaves like the function name
#and using the variablename we can make a function call.

#Lambda function to square a number

p=lambda x: x*x
print(p(10))
print(p(20))

#Same Task using Normal function:

def f2(x):
    return  x*x

print(f2(10))
print(f2(20))

#Note: A Lambda function can have any no of arguments but only one expression

a=lambda x,y: x*y #x,y are non-default arguments
print(a(10,20))     #non-keyword arguments
print(a(x=20,y=30)) #Keyword arguments

b=lambda x=30,y=20:x*y #here x,y are default arguments
print(b())
print(b(40))
print(b(30,40))

































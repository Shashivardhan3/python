

#Typecasting :Converting one collection to another
#Case 1: Converting a list to tuple

x=[10,20,30,40,50]
print(x,type(x))

y=tuple(x)
print(y,type(y))

#Case 2: Converting a tuple to list

x=(10,20,30,40,50)
print(x,type(x))

y=list(x)
print(y,type(y))

#Case 3: Converting a string to list
x="python"
print(x,type(x))

y=list(x)
print(y,type(y),len(y))

#Case 4: Converting a string to tuple
x="python"
print(x,type(x))

y=tuple(x)
print(y,type(y),len(y))

#Case 5: Converting a int to list
x=10
print(x,type(x))

'''
y=list(x)
print(y,type(y)) '''

y=[x]
print(y,type(y))

x1=10;x2=20;x3=30
z=[x1,x2,x3]

print(z,type(z))




































#call-by-value: Calling a function by providing some values

def display(x,y):
    z=x+y
    print("sum=",z)
display(10,20)   #call-by-value

#call-by-reference:calling a function by providing some reference

def show(a,b):
    c=a+b
    print("sum=",c)

p=30
q=40
show(p,q)

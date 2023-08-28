

#Arbitrary arguments or variable length arguments:

#here during fn call,we can specify more no of parameter values than
#specified in the fn definition.

#A asterisk (*) is placed before the variable name that holds
#multiple values,which is of tuple type

def display(name,*marks):  #fn def
    print(name,type(name))
    print(marks,type(marks))
    for p in marks:
        print(p)
display("Blake",75,65,90)  #fn call

print("\n\n\n")

#--------------------------------------------------------------------------------
def display1(name,*marks):
    print(name)
    x=1
    for p in marks:
        print("subject",x,":",p)
        x=x+1
        
display1("Blake",75,65,90)

print("\n")
#--------------------------------------------------------------------------------
#using while loop

def display1(name,*marks):
    print(name)
    x=1
    while(x<=len(marks)):
        for p in marks:
            print("subject",x,":",p)
            x=x+1
display1("Blake",75,65,90)









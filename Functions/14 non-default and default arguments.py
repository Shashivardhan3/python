#Types of Arguments:
'''
1.Non-default Arguments (or) positional Arguments
2.Default Arguments
3.Keyword Arguments
4.Non-Keyword Arguments
5.Arbitrary Arguments (or) Variable length Arguments
'''
#1.Non-default Arguments: Arguments Specified in the function definition and argument values
#                         compulsorily we need to provide within the function call

def display(name,age):  #non-default arguments
    print(name,age)

display("Ajay",35)
#display()
print('\n')
#2.Default Arguments: Arguments specified in the function definition with some default values
#here it is not compulsory to specify the values within the function call, if not provided
#then these default values will be taken

def show(name="Ajay",age=30): #Default arguments
    print(name,age)

show()
show("Rahul")
show("James",40)










    


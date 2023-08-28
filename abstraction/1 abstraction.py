
#Abstraction: The concept of hiding the properties(variables+methods) of one class from
#             other classes or outside classes is known as Abstraction.
#ex: S.v can be accessed from outside the class using classname,but i want to restrict this
#In order to hide the properties of a class, we use __ at the beginning of the property name
#ex: __x=10

class sample:
    __x=100    #now x is hidden and can be accessed from only within the class
    y=200
    print(__x)
    print(y)
    def display(self):
        print(sample.__x,type(sample.__x))
        print(sample.y,type(sample.y))
#end of the class
s1=sample()
s1.display()
#print(sample.__x)  #cant be accessed from outside the class
print(sample.y)

class test:
    a=300
    def show(self):
        print("a=",test.a)
        #print("x=",sample.__x)
        print("y=",sample.y)
t1=test()
t1.show()



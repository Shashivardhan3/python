#python doesnt support method overloading or constructor overloading

#Defining 2 or more methods or constructors with same name but with diff no of
#arguments is called as method overloading or constructor overloading.
class test:
    def __init__(self):
        self.a=10
        self.b=20
        print("a=",self.a)
        print("b=",self.b)
    def __init__(self,p,q):
        self.x=p
        self.y=q
    def display(self):
        ''' print("a=",self.a)
        print("b=",self.b)'''
        print("x=",self.x)
        print("y=",self.y)
t1=test()
t2=test(10,20)
t2.display()

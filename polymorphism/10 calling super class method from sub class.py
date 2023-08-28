

#sub class method calling super class method

class A:
    def m1(self):
        self.x=10
        print("x=",self.x)
        
class B(A):
    def m1(self):
        super().m1()
        self.y=20
        print("y=",self.y)


b1=B()
b1.m1()


#for overriding and executing userdefined logic only,no need of super,
#but to execute pre-defined logic and userdefined-logic,we need super

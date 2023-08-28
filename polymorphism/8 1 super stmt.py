
#super(): This stmt is used to call super class method or constructor through
#sub class method or constructor

class A:
    def __init__(self):
        print("from constructor A.....")
        self.x=10
        
class B(A):
    def __init__(self):
        super().__init__()           #Executes super class constructor
        print("from constructor B.....")
        self.y=20
        print("x=",self.x)
        print("y=",self.y)

b1=B()
#here first super class constructor executes followed by sub class constructor
#here both logics are executed userdefined logic(derived class logic) and base class
#logic

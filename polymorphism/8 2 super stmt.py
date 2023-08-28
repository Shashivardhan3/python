

#Accessing NSV of super class constructor from sub class constructor using super()

class A:
    def __init__(self):
        self.x=10
        print("from constructor A.....")
        
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
        
        print("from constructor B.....")


b1=B()
print(b1.x) # now it can be accessed    
print(b1.y)


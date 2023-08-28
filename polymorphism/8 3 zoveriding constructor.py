

class A1:
    def __init__(self):
        print("from constructor A1.....")
        
class A2:
    def __init__(self):
        print("from constructor A2.....")
        
class B(A1,A2):
    def __init__(self):
        super().__init__()           #Executes super class constructor
        
        print("from constructor B.....")


b1=B()

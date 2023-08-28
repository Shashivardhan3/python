

class x:
    def __init__(self,a,b):
        print("from constructor of x....")
        self.x=a
        self.y=b
        
class y(x):
    def __init__(self):
        print("from constructor of y....")
        
#y1=y()
y2=y(3,4)
x1=x(10,20)

#constructor oveloading happens---------->error

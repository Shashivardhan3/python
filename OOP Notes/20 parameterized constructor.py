
#Parameterized constuctor:
#A constructor with parameters is called as parameterized constructor.
class test:
    def __init__(self,a,b): #constructor with parameters
        self.x=a
        self.y=b
        
    def m1(self,p,q):
        r=p+q       #Local variables sum
        s=self.x+self.y #sum of NSV's
        print("r=",r)
        print("s=",s)

t1=test(10,20) #while creating object only,passing parameters and
               #assigning values to NSV's with different values
print(t1.x)
print(t1.y)
t1.m1(15,25)

t2=test(30,40)
print(t2.x)
print(t2.y)

t3=test(2.5,3.5)
print(t3.x)
print(t3.y)



















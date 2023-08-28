

#program to find the volume of a cube using a constructor.
class cube:
    def __init__(self):
        self.length=int(input("Enter length:"))
        self.breadth=int(input("Enter breadth:"))
        self.height=int(input("Enter height:"))
        
    def compute(self):
        self.volume=self.length*self.breadth*self.height
        print("VOLUME=",self.volume)
c1=cube() #constructor gets executed automatically. 
print(c1)
c1.compute()

print("Enter values for 2nd cube:")
c2=cube()
print(c2)
c2.compute()



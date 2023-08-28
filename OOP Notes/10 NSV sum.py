

class sample:
    '''class to compute sum'''
    a=10  #static variable
        
    def display(self,p,q):
        r=70       #local variable
        self.x=20  #NSV
        self.y=30  #NSV
        print("p=",p)
        print("q=",q)
        print("r=",r)
    def show(self):
        print("a=",sample.a)
        print("x=",self.x)
        print("y=",self.y)
        print("sum=",self.x+self.y)
#end of the class
s1=sample() #object creation stmt


print(s1)

s1.display(50,60) #s1 address will be stored in self of display
             #using this self only we are initializing x and y to 20 and 30
s1.show()

print(sample.a) #accessing SV from outside the class

#printing NSV's from outside the class

print(s1.x,type(s1.x),id(s1.x))
print(s1.y)

#modifying NSV from outside the class
s1.x=25
s1.y=35
print(s1.x,type(s1.x),id(s1.x))
print(s1.y)

#modifying sv
sample.a=15
print(sample.a)

#creating one more object

s2=sample()
print(s2)

s2.display(4,5)
s2.show()
print(s2.x,type(s2.x),id(s2.x))
print(s2.y)















    














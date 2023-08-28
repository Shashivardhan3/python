

#program illustrating Non-static variable

class sample:
    a=10 #Static variable
    b=20 #  "      "
    def display(self):
        self.x=30 #NSV's
        self.y=40 #NSV's
        print("a=",sample.a)
        print("b=",sample.b)
        print("x=",self.x)
        print("y=",self.y)
        #All the methods can access these SV's and NSV's

    def show(self):
        print("a=",sample.a)
        print("b=",sample.b)
        print("x=",self.x)
        print("y=",self.y)
#endo of the class
s1=sample() #object creation stmt
s1.display() # Here s1 address will be stored wthin the self of display and
             #using that self only we are initializing NSV's
s1.show()

#accessing SV's from outside the class using classname
print("a=",sample.a)
print("b=",sample.b)

#Accessing NSV from outside the class using reference variable
print("x=",s1.x)
print("y=",s1.y)

#static variables related to class
#non-static variable related to object
#NSV can be accesed within the class using self.
#NSV can be accessed from outside the class using object/ref.variable

#SV can be accesed inside/outside the class using classname
'''
1.How to define NSV----->within the class within the method------>self
2.How to access NSV within the class------>self
3.How to access NSV from outside the class------>ref.variable/object
4.who initializes the NSV----------------------->object
5.if there are 2 objects
  how many times memory allocated to NSV-------->2
6.does every object has its own NSV's ---------->yes

==q)why NSV should be defined within the method?
q)what happens if we define NSV outside the method?

q)how NSV's and objects are related?

Ans: object address------>passed to self of a method---->using that self only NSVs are created and initialized
     If NSV defined outside the method, the non-static variable cannot get the address of the object--
      -> and NSV cannot be created
'''
        
        
        
        
        

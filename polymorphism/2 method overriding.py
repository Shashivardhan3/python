

#method overriding: The concept of defining a method with same name and same no of
#parameters in both super class and sub class is known as method overriding
#here always derived class method overides the base class method
class x:
    def m1(self):
        print("from base class....")
        
class y(x):
    def m1(self):
        print("from derived class....")
y1=y()
y1.m1() #here subclass method is called or executed bcoz superclass method is
#overridden,To execute super class method also ,create super class object
x1=x()
x1.m1()

#Note: method overriding is seen only in inheritence




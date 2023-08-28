

within the class, we can represent data using
i.static variables.
ii.non static variables.

Static variables:The variables which are defined within the class and defined
 outside all the methods of a class are known as static variables.

ex: class sample:
          x=10 #static variable,defined within class and outside the method
          def m1(self):  #method
              print(sample.x)
    #end of the class
    print("x=",sample.x)
-------------------------------------------------------------------------------------------------------------------
 properties of static variable:

 1.The data which is common for all the objects,then it is recommended to
  represent by using static variables.
     ex:bank name---->SBI
        withdrawlimit-->25000
    
    data which is changing from one object to another object--->then
    use non-static variable
    ex:-ename,eid,designation,salary
        
 2.for static variable,only once memory is allocated,as it is initialized only once.
 
 3.A static variable can be accessed by all the methods of that class and also 
   by other classes
   ex:
       class sample:
           x=10  #SV
           def display():
               print(sample.x)
           def show():
               print(sample.x)
        Here x is a static variable which can be accessed by all the methods like
        display,show etc.
     
 4.A static variable always be accessed by using classname i.e from within the class
 or from outside the class also.
 ex:classname.staticvariable
 
 ex:
 class sample:
     x=10 #Static variable
     y=20 #Static variable
     def display(self):
         print(sample.x) #Accessing static variables using class name 
         print(sample.y)
     def show(self):     #here all the methods can access the SV
         print(sample.x)  
         print(sample.y)
#end of the class
print(sample.x)  #accessing SV from outside the class using classname
print(sample.y)

#---------------------------------------------------------------------------------------------         
#diff b/w function and method:

#        Function                                         Method
 1.Function alaways defined outside the class   1.Method always defined within the class

 2.Function called normally without object      2.Method always called using a object
    ex:  display()                                ex:  s1.display()

 3.For Function, no need of self Argument       3.Method compulsorily should have self argument

#----------------------------------------------------------------------------------------------     
#Difference b/w Static variable(SV) and NOn-Static Variable(NSV)
 
#              Static Variable(SV)                   Non-Static Variable(NSV)

1)for object to object if data is common       1)For object to object if data is changing 
  go for static variable                         go for Non-static variable
  ex:company="TCS"                               ex: ename=input("Enter the name:")


2)always defined outside the methods           2)Always defined within the methods

3)Static variable is no way related to         4)object is used to intialize a NSV
  object.                                      without object NSV cannot be created or initialized


4)SV--->only once memory is allocated          4)here multiple times memory is allocated
  i.e only once they are initialized             i.e multiple times they are initialized.
  ex:company="TCS"                               e1.eid=101
                                                 e2.eid=102
                                                 e3.eid=103
                                                 if 3 objects--->3 times NSV's are initialized
                                                 if n objects--->n times NSV's are initialized
  
  



















 

 












 

 
 

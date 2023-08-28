

#Parameterized constructor: A constructor with parameters is called as
#parameterized constructor
#Note: In parameterized constructor,how many arguments are provided then
#those many NSVs need to be defined.
class student:
    def __init__(self,name,age): #parameterized constructor
        self.stdname=name
        self.stdage=age
        #self.display()
        
    def display(self):
        print("NAME:",self.stdname)
        print("AGE:",self.stdage)
s1=student("Ajay",25)
s1.display()
s2=student("miller",28)
s2.display()
s3=student("Amar",26)
s3.display()

#Note: whenever object is created,it is initializing NSV's with
#different values



#hiding a method
class sample:
    __x=100       #hiding a sv
    
    def display(self):
        self.__y=200 #hiding a NSV
        print("x=",sample.__x)
        print("y=",self.__y)
        self.display2()
    def display2(self):
        self.z=sample.__x+self.__y
        print("z=",self.z)
        self.__display3()
    def __display3(self):   #hiding a method
        self.a=50
        print("a=",self.a)
s1=sample()
s1.display()
s1.display2()
#s1.__display3()
print(s1.a)
#print(sample.__x)
#print(s1.__y)
print(s1.z)
print(s1.a)





















class sample:
    __x=10
    def display(self):
        self.__y=20
        print("x=",sample.__x)
        print("y=",self.__y)
#end of the class
s1=sample()
s1.display()
#print("x=",sample.__x)
#print("y=",s1.__y)

        

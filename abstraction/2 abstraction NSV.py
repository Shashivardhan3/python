
#hiding static and NSV

class sample:
    __x=100           #hiding a sv
    def display(self):
        self.__y=200  #hiding a NSV
        print(sample.__x)
        print(self.__y)
s1=sample()
s1.display()
#print(sample.__x)   #S.V cant be accessed
#print(s1.__y)  #NSV cant be accessed



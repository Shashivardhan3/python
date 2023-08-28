class employee:
    """employee Application"""
    company="Infosys"  #static variable
    empcount=0
    def __init__(self,empname,empid,empsal,design="SE",*languages,**details):   #*-->tuple type **->dict type
   #how many constructor parameters are defined,those many
   #NSV's should be defined
        #data 
        self.empname=empname
        self.empid=empid
        self.empsal=empsal
        self.design=design
        self.languages=languages
        self.details=details
        employee.empcount=employee.empcount+1
           
    def displayemployee(self):
        print("NAME:",self.empname,"ID:",self.empid,"SALARY:",self.empsal,
        "DESIGNATION:",self.design,"LANGUAGES=",self.languages,self.details)
#end of class
emp1=employee("Scott",101,30000.00,"Manager","Eng","hindi",grade="A",age=25)
emp2=employee("Miller",102,40000.00,"Clerk","Eng","Telugu",dname="mrkt",city="pune")
emp3=employee("Blake",103,50000.00,"SE","Eng","Tamil",dno=11)

emp1.displayemployee()
emp2.displayemployee()
emp3.displayemployee()

print("Total No of Employees are:",employee.empcount)
print("COMPANY NAME:",employee.company)

x=[emp1,emp2,emp3]

for p in x:
    print(p.displayemployee())






              
              

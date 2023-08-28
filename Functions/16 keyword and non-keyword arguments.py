
#Keyword and non-keyword arguments:

#Keyword Arguments: During function call, with parameter name(keyword) passing value

#Non-keyword Arguments:During function call,without parameter name(Keyword) passing value

def emp(eid,ename,sal,desig,city="pune"):
    print(eid,ename,sal,desig,city)

emp(101,"James",30000,"Manager","Chennai")  #Non-keyword Arguments

emp(sal=50000,eid=102,ename="Miller",city="hyd",desig="professor")#Keyword Arguments

emp("Blake",103,"S/w Engineer","Mumbai",60000) #Valid but not recommended

emp(104,"John",70000,desig="Teacher",city="Mumbai")#non-keywords and keyword arguments

#emp(eid=105,ename="Amar",sal=15000,"Teacher","Pune")

#Note: we cannot specify keyword arguments before non-keyword arguments
#      i.e always specify non-keyword arguments first and then specify keywords

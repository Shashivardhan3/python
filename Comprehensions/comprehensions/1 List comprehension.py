#Comprehensios:
'''
1.List Comprehension
2.Tuple Comprehension ----->not supported
3.Set Comprehension
4.Dictionary Comprehension
'''

#1.List Comprehension : Creating a list from other iterable types
#Case 1: Creating a list from a range() function.
x=range(10)

y=[p for p in x]
print(y,type(y))

#ex:2
y=[p for p in range(10)]
print(y,type(y))

#ex3: I want only even values
y=[p for p in range(0,20,2)]
print(y,type(y))

#ex:4 We can also provide conditions(if-conditions)
y=[p for p in range(1,21) if(p%2==0)]
print(y,type(y))
#---------------------------------------------------------------------------------------------
#Case 2: Creating a list from a string

x="Good Morning Hyderabad"

#If we split a string,we get a list
y=x.split(" ")
print(y,type(y))

#ex:
y=[p for p in x.split(" ")]
print(y,type(y))

#ex:3
y=[p for p in "Hello World".split(" ")]
print(y,type(y))

#----------------------------------------------------------------------------------------------
#Case 3: Creating a list from a list

cities=["mumbai","chennai","delhi","hyderabad","pune"]

#Create a list in which each city starts with uppercase character
y=[p.capitalize() for p in cities]
print(y,type(y))

#Creating a nested list

y=[[p,p.upper(),len(p)] for p in cities]
print(y,type(y))

#---------------------------------------------------------------------------------------------
#Case 4: Creating a list from a tuple

emps=((101,"Miller",30000),(102,"Blake",40000),(103,"James",50000),(104,"Ajay",60000))

y=[p for p in emps]
print(y,type(y))

#-----------------------------------------------------------------------------------------------
#Case 5: Creating a list from a set

x={10,20,30,40,50}
y=[p for p in x]
print(y,type(y))














































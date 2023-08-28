#Set Comprehension: Creating a set from other iterable types

#Case 1: Creating a set from a range() function
x=range(10)
y={p for p in x}
print(y,type(y))
#--------------------------------------------------------------------------------------------
#Case 2 :Creating a set from a string

x="Good Morning Hyderabad"

y={p for p in x.split(" ")}
print(y,type(y))

#--------------------------------------------------------------------------------------------
#Case 3: Creating a set from a list

emps=["Ajay","Rohith","Miller","Blake","James"]

y={p for p in emps}
print(y,type(y))

#---------------------------------------------------------------------------------------------
#Case 4: Creating a set from a tuple
x=(10,20,30,40,50)
y={p for p in x}
print(y,type(y))
#---------------------------------------------------------------------------------------------
#Case 5: Creating a set from a set
x={10,20,30,40,50}
y={p for p in x}
print(y,type(y))















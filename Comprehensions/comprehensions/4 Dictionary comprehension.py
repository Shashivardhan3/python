
#Dictionary Comprehension: Creating a dictionary from other iterable types

#Case 1: Creating a Dictionary from a range function
x=range(1,9)

y={p:p**2 for p in x}
print(y,type(y))

#Case 2: Creating a Dictionary from a string
x="Good Morning India"

y={p:len(p) for p in x.split(" ")}
print(y,type(y))

#Case 3: Creating a Dictionary from a list
cities=["Mumbai","Chennai","Pune","Delhi","Hyd"]

y={p:len(p) for p in cities}
print(y,type(y))

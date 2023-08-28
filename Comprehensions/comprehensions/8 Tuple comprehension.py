#Accepting tuple of values from the user keyboard

print("Enter marks of 5 subjects:")
y=tuple(int(p) for p in input().split(" "))
print(y,type(y))

print("TOTAL MARKS=",sum(y))

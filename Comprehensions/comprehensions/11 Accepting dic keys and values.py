#Accepting Dictionary keys and values from the user keyboard
#Accept 2 lists, one for keys and other for values
#merge these 2 lists using zip() to create a dictionary

subjects=[]
marks=[]

print("Enter subject names as Keys:")
for p in range(1,6):
    key=input("Enter the Name of subject"+str(p)+":")
    subjects.append(key)

print("Enter the marks as values:")
for p in range(0,5):
    value=int(input("Enter the marks of"+subjects[p]+":"))
    marks.append(value)

print(subjects)
print(marks)

#merging these 2 lists using zip() function
x=zip(subjects,marks)
print(x,type(x))

y=list(x)
print(y,type(y))

z=dict(y)
print(z,type(z))
















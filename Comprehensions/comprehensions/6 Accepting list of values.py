#Accepting list of values

marks=[]
for p in range(1,6):
    x=int(input("Enter marks of Subject"+str(p)+":"))
    marks.append(x)
print(marks)
print("TOTAL MARKS=",sum(marks))

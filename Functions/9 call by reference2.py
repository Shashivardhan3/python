#call-by-reference:

def display(list1):
    list1.append(60)
    print(list1,id(list1))

list1=[10,20,30,40,50]
print(list1,id(list1))
display(list1)
print(list1,id(list1))

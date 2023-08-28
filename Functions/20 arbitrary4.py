

#to overcome above problem,we assign values to q and r using keyword arguments
#or default arguments.

def display(*p,q,r=45):
    print(p,type(p))
    print(q,type(q))
    print(r,type(r))

display(10,20,q=30)
display(10,20,30,q=40,r=50)
display((10,20,30),q=40,r=50)
display((10,20,30),(40,50),q=40,r=50)




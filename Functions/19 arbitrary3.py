
def display(*p,q,r):
    print(p,type(p))
    print(q,type(q))
    print(r,type(r))
    
display(10,20,30)
display(10,20,30,40,50)
display(10,20)

#error-----------> becoz all values are taken by p as tuple
#values of q & r are missing

#Note: we can take arbitrary argument as the first argument provided that we use
#default or keyword arguments

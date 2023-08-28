#Non-default and default arguments:

def display(name,city="pune"):
    print(name,city)

#display()
display("Ajay")
display("Chennai")
display("John","Chennai")

#default and non-default arguments:
'''
def show(name="Ajay",city):
    print(name,city)
#show()
show("Pune")
show("James") '''

#Note: We cannot specify default arguments before non-default arguments
#      Always non-default should be specified first and then default arguments as ex:1

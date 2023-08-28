#Modifying the global variables from within the function

x=10          #Global variable
def display():
    global x #forward declaration, This declarations says that the global variable value is
             #going to be modified in the later stmts
    x=15
    print(x)

def show():
    print(x)

show()
display()
show()




    

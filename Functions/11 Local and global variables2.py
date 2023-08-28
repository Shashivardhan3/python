
#Local and global variables with same name

x=10             #Global variable

def display():
    x=20         #Local variable
    print(x)     #always local variables will be given preference over global variables

def show():
    print(x)
    
display()
show()

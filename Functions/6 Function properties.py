#Function properties:

#1.A Function can be called for multiple times

def display():
    print("hello....")
    print("Good Morning!!!")

display()
display()
display()

#adv: Code re-usability
#---------------------------------------------------------------------------------------------
#2. The order in which the functions are defined and the order in which they are called need
#   not be the same.

def English():
    print("ABCDEFGHIJ.........")

def Maths():
    print("123456789........")

def Chemistry():
    print("H2O is the chemical name of water")

Maths()
Chemistry()
English()

#---------------------------------------------------------------------------------------------
#3. A Function can call another function

def hyd():
    print("Hello Hyderabad!!!")
    mumbai()

def mumbai():
    print("Hello mumbai!!!")
    
hyd()

#---------------------------------------------------------------------------------------------
#4. We cannot call a function before its definition
'''
display1().
display2()

def display1():
    print("hello")

def display2():
    print("Good Morning!!!")
'''
#---------------------------------------------------------------------------------------------
#5.We can define a function in another Function


def compute():
    print("Good morning!!!")
    def show():
        print("Good Evening!!!")
    show()

compute()
#show()

















    


























    

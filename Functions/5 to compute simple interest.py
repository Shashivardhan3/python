#Function to compute Simple interest

def compute():
    '''SIMPLE INTERSET'''
    p=int(input("Enter the principle amount:"))
    t=int(input("Enter the time period:"))
    r=float(input("enter the rate of interest:"))
    si=(p*t*r)/100
    print("SIMPLE INTEREST=",si)

compute()

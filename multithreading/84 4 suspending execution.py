import threading
import time        #time module----> for suspending the execution
class x(threading.Thread):
    def run(self):   # thread 2
        time.sleep(10)  #delay or suspend time in seconds, sleep() present in time module for suspending
        i=1
        while(i<=30):  #execution for some time
            print("PYTHON")
            i=i+1
        time.sleep(15)
        for p in range(30):
            print("hello")
    def m1(self):
        print("Hai")
class y(threading.Thread):  
    def run(self):   # thread 3
        time.sleep(20)
        j=1
        while(j<=30):
            print("JAVA")
            j=j+1
        time.sleep(25)
        for p in range(30):
            print("Good morning....") 
x1=x()        #main thread
x1.start() #thread 2 starts and get suspended,meanwhile thread 3 executes and after suspend time is finished 
y1=y()     #again thread 2 excutes ,if u give less suspend time then we get mixed output
y1.start()
x1.m1()

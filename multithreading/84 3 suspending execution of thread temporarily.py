# Temporarily suspending the execution of a thread:
#we can suspend the execution of thread temporarily for some time by calling sleep() of time module.

import threading
import time        #time module----> for suspending the execution
class x(threading.Thread):
    def run(self):   # thread 2
        time.sleep(10)  #delaytime or suspend time in seconds, sleep() present in time module for
                        #suspending execution for some time.
        for p in range(1,101):  
            print(p)
            
class y(threading.Thread):
    def run(self):   # thread 3
        for q in range(101,201):
            print(q)


x1=x()        #main thread
x1.start() #thread 2 starts and get suspended,meanwhile thread 3 executes ,after suspend time is finished 
y1=y()     #again thread 2 exeecutes ,if u give less suspend time then we get mixed output
y1.start()


#If multiple threads are running,if we get error in one thread, then will it effect the other
# thread execution?

#Everytime not only the run() method acts as a thread,but normal method can also behave like a thread,
#but should be called from run() method


#If a class have got 10 objects,then we have 10 threads

import threading
import time        
class x(threading.Thread):
    def run(self):   # thread 2
        time.sleep(10)  
        for p in range(1,11):  
            print(p)
         
class y(threading.Thread):
    def run(self):   # thread 3
        for q in range(11,21):
            print(q)
t1=x()        
t1.start() 
t2=y()     
t2.start()
t3=x()
t3.start()
t4=y()
t4.start()

#here totally 5 threads, 1 main thread+ 4 threads

#Note: If 'n' objects----->then n+1 threads

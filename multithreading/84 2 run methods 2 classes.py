

#If i want to execute 2 logics--------->means keep in 2 run()methods--->means take 2 classes
#------>means 2 Threads
import threading
class x(threading.Thread):
    def run(self):   # thread 2
        for p in range(100):
            print(p)

            
class y(threading.Thread):
    def run(self):   # thread 3
        for q in range(100,200):
            print(q)
            #print(a)
            
x1=x()        #main thread
x1.start()
y1=y()
y1.start()
#x1.start()    #Threads can only be started once
for r in range(200,300):
    print(r)
for s in range(300,400):
   print(s)

#here total 3 threads--->1.main thread   2.'X' class thread  3. 'Y' class thread 

#If multiple threads are running,if we get error in one thread, then will it effect the other
# thread execution?-------->

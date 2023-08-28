

#In order to execute the run()method logic as a thread,we need to call run()method
#through the start()method of Thread class,then they r executed parallely.

import threading

class x(threading.Thread):
    def run(self):   # thread 2
        for p in range(100):
            print(p)
        #for s in range(200,300):
        #    print(s)
            
#end of class
x1=x()        #main thread
x1.start()
for q in range(100,200):
    print(q)
    

#By default python interpreter creates one thread i.e main thread,
#first main thread starts executing,meanwhile remaining threads get executed,mixed execution
#here both threads are executed parallely



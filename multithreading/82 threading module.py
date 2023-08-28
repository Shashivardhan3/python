#Threading module:
#In threading module,we have a pre-defined class called Thread,which has
#a method called run()method,

#to make a logic as thread ,keep that logic in run()method,we will overide
#the run()method of Thread class and run()method logic behaves like a thread.

import threading  #threading is a built-in module
class x(threading.Thread): #userdefined class exending Thread class(built-in)
    def run(self):   # thread 2   ----->here run method overides the run() method of Thread class
        for p in range(10):
            print(p)
#end of class
x1=x()        #main thread
x1.run()
for q in range(10,20):
    print(q)

#import threading
#help(threading.Thread)
    
#stmts outside  the class are treated as main thread.
#stmts or code within run() method is treated as 2nd thread,

#if u execute the program, no multithreading is performed bcoz
#here run()executed as normal method,but not executed as a thread,
#in above program there r 2 threads,but not running parallely bcoz ,
#they are executed normally,so to execute parallely,use start()method as fncall
#instead of run()
            



#3.setName():To set our own name for a thread

from threading import *

print(current_thread().getName())
current_thread().setName("demo thread")
print(current_thread().getName())




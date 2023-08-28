
#MULTITHREADING :
#The process of executing 2 or more threads(logics)simultaneously is known as MultiThreading.

class x:
    def m1(self):
        for p in range(10):
            print(p)
    def m2(self):
        for q in range(10,20):
            print(q)
x1=x()
x1.m1()
x1.m2()
#here 1st m1() method logic executes an then
#m2() method logic is executed,here execution is sequential,if i want parallel then go
#for multithreading.


#generally processor executes the programs,it is an electronic circuit,it understands only
#power signals,this electronic circuit executes only one stmt at a time(sequentially),
#wont execute parallely.


#in the program if we make m1 as one thread and m2 as 2nd thread, when m1 is waiting for i/p,
#meanwhile m2 logic will be executed and again switches to m1 thread,if issue in m1 again,then
#continues with m2,untill problem resolved,means internally only one thread is executed
#in processor,


#process : A program under execution
#Thread: It is a part of program or logic,which executes simultaneously along with the other
#part of the program

#reduce() : for cummulative operations
#reduce() function takes 2 arguments:
#    1.lambda function
#    2.Iterable type like list

from functools import reduce
#ex:1
list1=[1,2,3,4,5,6]

res1=reduce(lambda x,y:x+y,list1)
print(res1)

#o/p:
#(((((1+2)+3)+4)+5)+6) =21

#ex:2  To find the largest number
res2=reduce(lambda x,y:x if(x>y) else y,list1)
print(res2)

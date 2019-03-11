#processpy
#单进程测试

from test import *
from multiprocessing import Process
from time import time,ctime
def wr():
    for x in range(10):
        write()
        read()

def count1():
    x = 1
    y = 1
    for x in range(10):
        count(x,y)


p = Process(target=wr)
t1 = time()
print(t1)
p.start()
p.join()
t2 = time()
print(t2)

t = t2-t1
# print("count1消耗时间",t)
print("wr消耗事件",t)



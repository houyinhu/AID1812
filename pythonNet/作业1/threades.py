#threades.py
#多线程测试
from test import *
from multiprocessing import Process
from threading import Thread
from time import time,ctime
def wr():
    write()
    read()

def count1():
    x = 1
    y = 1
    count(x,y)

threads = []
t1 = time()
print(t1)
for x in range(10):
    t = Thread(target=wr)
    threads.append(t)
    t.start()

for x in threads:
    x.join()
t2 = time()
print(t2)

t = t2-t1
# print("count1消耗时间",t)
print("wr消耗事件",t)


#process1.py
import multiprocessing as mp
from time import sleep
import os

#全局变量
a = 1
#编写进程函数
def fun():
    sleep(10)
    global a
    print("a = ",a)
    a = 10000
    print("子a改变后:",a)
    print("子pid:",os.getpid())
    print("子进程执行的事件")

#创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start()
sleep(2)
print("父进程事件")
#回收进程
p.join(1)
print("==========")
print("父a:",a)
print("子pid:",os.getpid())




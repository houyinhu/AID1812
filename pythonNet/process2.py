from multiprocessing import Process
from time import sleep
import os

def th1():
    #name = input("数图")#子进程不能标准输入
    sleep(3)
    print("吃饭")
    print(os.getppid(),'---',os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'---',os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'---',os.getpid())

things = [th1,th2,th3]
processs = []
for th in things:
    p = Process(target=th)
    processs.append(p)#用列表保存进程对象
    p.start()
for i in processs:
    i.join()
    print(i,"被回收")



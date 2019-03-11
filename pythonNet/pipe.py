#pipe.py
from multiprocessing import Pipe,Process
import os,time

#创建管道对象
fd1,fd2 = Pipe()

def fun(name):
    time.sleep(1)
    #向管道写入内容
    fd1.send({name:os.getpid()})

jobs = []
for i in range(5):
    # time.sleep(0.1)
    p = Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    #读取管道内容
    data = fd2.recv()
    print(data)

for i in jobs:
    i.join()




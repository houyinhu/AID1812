#pool.py
from multiprocessing import Pool
from time import sleep,ctime
from multiprocessing import Pipe,Process
import os,time

#创建管道对象
fd1,fd2 = Pipe()

def fun(name):
    time.sleep(1)
    #向管道写入内容
    fd1.send({name:os.getpid()})



result = []
#创建进程池
pool = Pool(4)

#向进程池添加事件
for i in range(10):
    msg = 'hello %d'%i
    r = pool.apply_async(func=fun,args=(msg,))
    result.append(r)#存储函数事件对象

for i in range(5):
    #读取管道内容
    data = fd2.recv()
    print(data)


#关闭进程池
pool.close()

#回收进程池
pool.join()


    







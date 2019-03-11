#pool_map.py

from multiprocessing import Pool
from time import sleep,ctime

def fun(n):
    sleep(1)
    return n * n

print(ctime())
pool = Pool(2)
#使用map将函数放入进程池
r = pool.map(fun,[1,2,3,4,5])

pool.close()

pool.join()

print("结果：",r)
print(ctime())


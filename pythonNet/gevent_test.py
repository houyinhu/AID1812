#gevent_test.py
import gevent
import time

def foo():
    print("Running foo")
    gevent.sleep(3)
    print("Foo again")

def bar():
    print("Running bar")
    gevent.sleep(2)
    print("Bar again")

f = gevent.spawn(foo)
b = gevent.spawn(bar)

gevent.joinall([b,f])

# from multiprocessing import Process
# import time,os

# def pro_func(name,age,**kwargs):
#     for i in range(5):
#         print("子进程正在运行中,name=%s, age=%d, pid=%d" %(name,age,os.getpid()))
#         print(kwargs)
#         time.sleep(0.2)
        

# if __name__ == '__main__':
#     # 创建 Process 对象
#     p = Process(target=pro_func,args=('小明',18),kwargs={'m': 20})
#     # 启动进程
#     p.start()
#     time.sleep(1)
#     # 1 秒钟之后，立刻结束子进程
#     p.terminate()
#     p.join()

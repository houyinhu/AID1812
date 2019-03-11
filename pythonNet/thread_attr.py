#thread_attr.py
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name='Tarena')
print()
#线程名称
print("Thread name:",t.name)
t.setName('Tedu')
print("Thread name:",t.getName())

#设置daemon为True
t.setDaemon(True)

print(t.is_alive())

t.start()
#查看线程生命周期
print('alive:',t.is_alive())
t.join()






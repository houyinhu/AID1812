#child_child.py
#创建二级子进程处理僵尸
import os
from time import sleep
def f1():
    sleep(3)
    print("吃元宵...")

def f2():
    sleep(4)
    print("处理南北甜咸之争...")

import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("创建二级子进程")
    p = os.fork()
    if p == 0:
        f2()#二级子进程做另一件事
    else:
        os._exit(0)
else:
    os.wait()#等待一级子进程退出
    f1()






#fock_waitpid.py
import os
from time import sleep

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(2)
else:
    #非阻塞等待
    while True:
        pid,status = os.waitpid(-1,os.WNOHANG)
        if pid != 0:
            break
        sleep(2)
        print("做了其他事情",pid)
    while True:
        print("完成父进程其他事件")
        sleep(2)
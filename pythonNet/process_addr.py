#process_addr.py
from multiprocessing import Process
from time import sleep,ctime
import os

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

p = Process(target = tm)

p.daemon = True

p.start()
print("Process name:",p.name)
print("Process PID:",p.pid)
print("Process pPID:",os.getppid())
print("alive:",p.is_alive())

p.join(2)
print("Process PID:",os.getpid())




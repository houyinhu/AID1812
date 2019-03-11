#get_pid.py

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID :",os.getpid())
    print("Get parent pid:",os.getppid())
    print(pid)
else:
    print("Parent PID:",os.getpid())
    print("Get Child pid:",pid)
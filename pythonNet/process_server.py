#process_server.py
from multiprocessing import Process
from socket import *
import os,signal
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#客户端处理函数
def handle(c):
    print("Conect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
    os._exit()


#创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

#循环等待客户端连接
while True:
    try :
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print("Error:",e)
        continue
    
    #创建进程处理客户端请求
    p = Process(target=handle,args=(c,))
    p.daemon = True
    p.start()
    













#block_io.py
from socket import *
from time import sleep,ctime

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(5)

#设置非阻塞状态
# 方法一
# sockfd.setblocking(False)
#方法二
sockfd.settimeout(2)

while True:
    print("Waitting for connect...")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError:
        # sleep(2)
        print("%s connect error"%ctime())
        # continue
    else:
        while True:
            msg = connfd.recv(1024)
            if not msg:
                break
            print("Connect from",addr)
            connfd.send("好".encode())



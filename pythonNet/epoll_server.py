#epoll_server.py
from socket import * 
from select import *

#创建关注的io
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8880))
s.listen(4)

#创建poll对象
p = epoll()
#建立查找字典
fdmap = {s.fileno():s}

#注册IO
p.register(s,EPOLLIN|EPOLLERR)

#循环监控
while True:
    events = p.poll()   #阻塞
    print("你有要处理的IO")
    #遍历列表,处理IO
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的注册IO
            p.register(c,EPOLLIN|EPOLLHUP|EPOLLET)
            fdmap[c.fileno()] = c
        # elif event & EPOLLHUP:
        #     print("客户端退出")
        #     p.unregister(fd)  #取消关注
        #     fdmap[fd].close()
        #     del fdmap[fd]

        # elif event & EPOLLIN:
        #     data = fdmap[fd].recv(1024)
        #     print("Receive:",data.decode())
        #     data = '收到消息'
        #     fdmap[fd].send(data.encode())




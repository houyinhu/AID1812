#select_test.py
from select import select
from socket import *
from sys import stdin
from time import ctime
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',9999))
sockfd.listen(4)

rlist = [sockfd,stdin]
wlist = []
xlist = []

f = open('log.txt','at')

while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    for r in rs:
        if r is sockfd:
            c,addr = sockfd.accept()
            rlist.append(c)
        elif r is stdin:
            f.write("%s  %s\n"%(ctime,r.readline()))
            f.flush()

        else:
            data = c.recv(1024)
            if not data:
                rs.remove()
                c.close()
                continue
            f.write("%s  %s \n"%(ctime,data.decode()))
            c.send("收到".encode())
            f.flush()
        
            



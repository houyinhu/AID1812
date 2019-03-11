#test_select_server.py

from select import select
from socket import *
from sys import stdin

#创建套接字作为关注的io
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9999))
s.listen(5)


rlist = [s,stdin]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for i in rs:
        if i is stdin:
            name = stdin.readline()
            try:
                f = open('s1.txt','at')
                f.write(name)
                f.flush()
            except :
                print("保存文件信息失败")
            else:
                print("保存成功")

        elif i is s:
            c,addr = s.accept()
            print("连接",addr)
            rlist.append(c)
        else:
            data = i.recv(1024)
            if not data :
                rlist.remove(i)
                i.close()
                continue
            try:
                f = open('s1.txt','at')
                f.write(data.decode())
                f.flush()
            except :
                print("保存文件信息失败")
            msg = "收到信息"
            i.send(msg.encode())
            
    for w in ws:
        print(name)
    for x in xs:
        pass




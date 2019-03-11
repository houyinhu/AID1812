#unix_recv.py
from socket import *
import os
#确定套接字文件
sock_file = './sock'

#判断一个文件是否存在，存在就删除
if os.path.exists(sock_file):
    os.remove(sock_file)

#创建套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定套接字文件
sockfd.bind(sock_file)

#监听，连接
sockfd.listen(3)

while True:
    c,address = sockfd.accept()
    print('连接',address)

    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()  



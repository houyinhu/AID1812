#udp.server.py

from socket import *
# 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
server_addr = ('0.0.0.0',9999)
sockfd.bind(server_addr)

while True:
    #接受消息
    print("等待")
    data,addr = sockfd.recvfrom(1024)
    print("Receive from %s:%s"%(addr,data.decode()))

    #发送消息
    data = "Thank for your mag"
    n = sockfd.sendto(data.encode(),addr)

#关闭套接字
sockfd.close()
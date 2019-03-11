from socket import *
#创建套接字

sockfd = socket()

#发起连接
server_addr = ('127.0.0.1',6666)
sockfd.connect(server_addr)

while True:
    #发消息
    data = input(">>")
    sockfd.send(data.encode())
    if data == '':
        break

    #收消息
    data = sockfd.recv(1024)
    print("From server:",data.decode())

#关闭套接字
sockfd.close()



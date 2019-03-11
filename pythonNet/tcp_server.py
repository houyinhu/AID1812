import socket

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',6666))

#设置监听
sockfd.listen(5)

while True:
    #等待处理客户端连接
    print("Waiting foconnect...")
    try:
        connfd,addr = sockfd.accept()  
        print(addr)
    except KeyboardInterrupt:
        print("Server exist")
        break
    print("Connect f .rom ",addr)#打印客户端地址

    while True:
        #收消息
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive message:",data.decode())

        #发消息
        n = connfd.send("Receive your message!!".encode())
        print("Send %d butes"%n)

#关闭套接字
connfd.close()
sockfd.close()





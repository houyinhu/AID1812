from socket import * 

#服务器地址
host = '127.0.0.1'
port = 9999
addr = (host,port)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#收发消息
while True:
    #发送消息
    data = input("Msg＞＞")
    if not data:
        break
    sockfd.sendto(data.encode(),addr)

    #接受消息
    msg,addr = sockfd.recvfrom(1024)
    print("Receive from server:",msg.decode())

sockfd.close()


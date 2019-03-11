from socket import *

sockfd = socket(AF_UNIX,SOCK_STREAM)

sock_file = './sock1'
sockfd.connect(sock_file)
while True:
    data = input("请输入")
    sockfd.send(data.encode())
sockfd.close()



from socket import *
import os,sys
import signal
def main():
    sockfd = socket(AF_INET,SOCK_STREAM)
    sockfd.getsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('172.88.2.247',8888))
    sockfd.listen(5)
    while True:
        connfd,address = sockfd.accept()
        print("来自客户端",address)
        data = connfd.recv(1024)
        connfd.send(b'hao')


if __name__ == '__main__':
    main()
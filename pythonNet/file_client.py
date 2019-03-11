#file_client
from socket import *

sockfd = socket()


server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

f = open('a1.txt',encoding='utf8')

while True:

    data = f.readlines()
    if not data:
        break
    line = ''.join(data)

    sockfd.send(line.encode())
    data = sockfd.recv(1024)
    print("服务器：%s"%data.decode())
    
sockfd.close()



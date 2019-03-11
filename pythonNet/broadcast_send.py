
from socket import *
from time import sleep

#目标地址
dest = ('127.0.0.1',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = '你好'

while True:
    sleep(2)
    s.sendto(data.encode(),dest)

s.close()



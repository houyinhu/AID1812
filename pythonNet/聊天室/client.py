#chat_client.py
from socket import *
import os,sys
import signal

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

ADDR = ('127.0.0.1',8888)

#发送消息
def send_msg(s,name):
    while True:
        text = input("发送消息：")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)
        if text == '#':
            os._exit(2)

def recv_msg(s):
    while True:
        data,address = s.recvfrom(2048)
        if data.decode() == '#':
            break
        print(data.decode())

#创建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名：")
        msg = "L " + name 
        #发送请求给服务的
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data,address = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("你已进入聊天室")
            break
        else:
            print(data.decode())
    
    #创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(s,name)
    else:
        
        recv_msg(s)

if __name__ == '__main__':
    main()










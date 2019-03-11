#chat_server.py
'''
Chatroom
env:python3.5
exc:socket and fork
'''

from socket import *
import os,sys

#用于存储用户{name:addr}
user = {}

#处理登录
def do_login(s,name,addr):
    if (name in user) or (name == "管理员消息"):
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr)

    #通知其他人
    msg = '欢迎%s来到聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name] = addr

#处理发送消息
def do_chat(s,name,text):
    msg = '\n%s : %s'%(name,text)
    for x in user:
        s.sendto(msg.encode(),user[x])

#处理客户端退出
def do_quit(s,name):
    msg = '\n%s退出了聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    else:
        s.sendto(b'EXIT',user[i])
    #将用户删除
    del user[name]

#处理客户端请求
def do_requests(s):
    while True:
        data,addr = s.recvfrom(1024)
        msglist = data.decode().split(' ')
        #区分请求类型
        if msglist[0] == 'L':
            do_login(s,msglist[1],addr)
        elif msglist[0] == 'C':
            #从新组织消息内容
            text = ' '.join(msglist[2:])
            do_chat(s,msglist[1],text)
        elif msglist[0] == 'Q':
            do_quit(s,msglist[1])

        print(data.decode())

#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    #创建单独进程用于发送管理元消息
    pid = os.fork()
    if pid < 0:
        print("Error")
        return
    elif pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员消息 "+msg
            s.sendto(msg.encode(),ADDR) 
    else :
         #处理各种客户端请求
        do_requests(s)
    

if __name__ == '__main__':
    main()








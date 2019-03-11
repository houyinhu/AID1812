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
    if name in user:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr)

    #通知其他人
    msg = '欢迎%s来到聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name] = addr

def do_chat(s,name,text):
    msg = '%s : %s'%(name,text)
    for x in user:
        s.sendto(msg.encode(),user[x])

#处理退出
def do_quit(s,name): 
    msg = '%s退出聊天室'%name
    for x in user:
        s.sendto(msg.encode(),user[x])


#处理客户端请求
def do_requests(s):
    while True:
        data,addr = s.recvfrom(1024)
        msglist = data.decode().split(' ')
        #区分请求类型
        if msglist[0] == 'L':
            do_login(s,msglist[1],addr)
        elif msglist[0] == 'C':

            #处理退出
            if '#' == msglist[2]:
                s.sendto('#'.encode(),user[msglist[1]])
                del user[msglist[1]]
                do_quit(s,msglist[1])
                continue
            #从新组织消息内容
            text = ' '.join(msglist[2:])
            do_chat(s,msglist[1],text)
        

        print(data.decode())

#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    #处理各种客户端请求
    do_requests(s)

if __name__ == '__main__':
    main()








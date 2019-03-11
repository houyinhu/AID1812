#dictionary_client.py
from socket import *
import pymysql,time
from multiprocessing import Process

#登录
def do_in():
    sockfd = socket()    
    sockfd.connect(('127.0.0.1',8888))
    sockfd.send('I'.encode())
    while True:
        name = input("请输入姓名>>")
        if name == '#' :
            return
        passwd = input("请输入密码>>")
        if passwd == "#":
            return
        np = name+' '+passwd
        sockfd.send(np.encode())
        data = sockfd.recv(1024).decode()
        if data == 'not':
            print("登录失败")
            continue
        elif data == 'ok':
            print("登录成功")
            break
    while True:
        print("================")
        print("query----查询单词")
        print("history--历史记录")
        print("canout---注销")
        print("================")
        cmd = input("请选择你的操作>>")
        if cmd == 'query':
            do_query(sockfd)
        elif cmd == 'history':
            do_history(sockfd)
        elif cmd == 'canout':
            sockfd.send(b'#')
            return

def do_history(s):
    s.send(b'H')
    while True:
        data = s.recv(1024).decode()
        if data == '#':
            break
        print(data)

def do_query(s):
    s.send(b"Q")
    while True:
        query = input("请输入查询单词>>")
        if query == '#':
            s.send(b'#')
            break
        s.send(query.encode())
        msg = s.recv(1024).decode()
        if msg == '#':
            print("查不到此单词")
            continue
        else:
            print(msg)



#注册
def do_re():
    sockfd = socket()
    sockfd.connect(('127.0.0.1',8888))
    sockfd.send("R".encode())
    data = sockfd.recv(1024).decode()
    if data == 'OK':
        while True:
            name = input("请输入姓名")
            if name == '#' :
                sockfd.send('#'.encode())
                return
            passward = input("请输入密码")
            if passward == '#':
                sockfd.send('#'.encode())
                return
            q = input("确定注册？ f:重新输入，q:确认注册")
            if q == 'q':
                np=name+' '+passward
                sockfd.send(np.encode())
                isname = sockfd.recv(1024).decode()
                if isname == 'not':
                    print("姓名已存在，请重新输入")
                    continue
                elif isname == 'ok':
                    print("注册成功，2秒后跳转到主页面")
                    time.sleep(2)
                    break
                else:
                    print("注册失败")
                    continue
            else:
                continue
           
    sockfd.close()


if __name__ == '__main__':
    while True:
        print("in--登录")
        print("re--注册")
        print("out--退出")
        x = input("请选择你的操作>>")
        if x == 'in':
            do_in() 
            continue
        elif x == 're':
            do_re()
            continue
        elif x == 'out':
            break
        else:
            print("-----请输入正确操作------")
            continue




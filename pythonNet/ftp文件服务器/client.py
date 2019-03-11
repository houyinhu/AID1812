from socket import *
import os,sys,time


def do_list(sockfd):
    data = sockfd.recv(1024).decode()
    if data == 'OK':
        data = sockfd.recv(4096).decode()
        for x in data.split(','):
            print(x)

def do_get(sockfd):
    data = input("请输入要下载的文件：")
    sockfd.send(data.encode())
    m = sockfd.recv(1024).decode()
    if m == 'OK':
        try:
            f1 = open(data,'wb')
        except OSError:
            print("打开错误")
        else:
            while True:
                data =  sockfd.recv(1024)
                if data == b'#':
                    print("下载完成")
                    break
                f1.write(data)  
                f1.flush 
    else:
        print(m)

def do_put(sockfd):
    data = input("请输入要上传的文件")
    filename = data.strip().split('/')
    if len(filename) == 1:
        name = filename[-1]
    else:
        name = filename[-1]
        namelus = filename[0:-1]
        namelu = '/'.join(namelus)
    sockfd.send(name.encode())

    data1 = sockfd.recv(1024).decode()
    if data1 == 'OK':
        try:
            f1 = open(data,'rb')
        except OSError:
            print("上传文件失败")
        else:
            while True:
                line = f1.read()
                if not line:
                    time.sleep(0.5)
                    sockfd.send(b'#')
                    print("上传完成")
                    break
                sockfd.send(line)
    else:
        print(data1)
        return
    
def main():
    sockfd = socket()
    sockfd.connect(('127.0.0.1',8886))
    while True:
        print("-------------")
        print("list-查看文件列表")
        print("get-下载文件")
        print("put-上传文件")
        print("quit-退出")
        print("-------------")
        data = input("请输入你的操作选择>>")
        if data == 'list':
            sockfd.send('list'.encode())
            do_list(sockfd)
        elif data == 'get':
            sockfd.send('get'.encode())
            do_get(sockfd)
        elif data == 'put':
            sockfd.send('put'.encode())
            do_put(sockfd)
        elif data == 'quit':
            sockfd.send('quit'.encode())
            sys.exit()
        else:
            print("请输入正确操作")


if __name__ == '__main__':
    main()






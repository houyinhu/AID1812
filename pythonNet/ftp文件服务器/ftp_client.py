#ftp_client.py
from socket import *
import sys,os
import time 

#具体功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list(self):
        self.sockfd.send(b'L')#发送请求
        #等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split(',')
            for file in files:
                print(file)
        else:
            #无法完成
            print(data)
    
    def do_get(self,filename):
        self.sockfd.send(('G %s'%filename).encode())
        #等待反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            try:
                fd = open(filename,'wb')
                while True:
                    data = self.sockfd.recv(1024)
                    if data == b'#':
                        break
                    fd.write(data)
                fd.close()
            except IOError:
                print("打开文件失败")
        else:
            print(data)
    
    def do_put(self,filename):
        name1 = filename.strip().split('/')[-1]
        name2 = filename.strip().split('/')[0:-1]
        for x in filename.split('/'):
            if x == name1:
                break
            name2+=x+'/'
        print(name1,'----',name2)
        try:
            if name1 in os.listdir(name2):
                self.sockfd.send(('P %s'%name1).encode())
                #等待反馈
                data = self.sockfd.recv(128).decode()
                if data == 'OK':
                    f1 = open(filename,'rb')
                    while True:
                        line = f1.read(1024)
                        if not line :
                            time.sleep(1)
                            self.sockfd.send(b'#')
                            break
                        self.sockfd.send(line)  
                    print("完成") 
                else:
                    print("服务器不能上传文件")
        except IOError:
            print("文件操作失败")
        except:
            print("找不到此文件")
 
          
    
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

#网络连接
def main():
    sockfd = socket(AF_INET,SOCK_STREAM)
    try:
        sockfd.connect(('127.0.0.1',8888))
    except Exception as e:
        print("连接异常",e)
        return
    
    #创建文件处理类对象
    ftp = FtpClient(sockfd)

    print("list-查看文件列表")
    print("get file-下载文件")
    print("put file-上传文件")
    print("quit-退出")

    while True:
        data = input("请选择你的操作>>")
        if data == 'list':
            ftp.do_list()
        elif data[0:3] == 'get':
            filename = data.split()[-1]
            ftp.do_get(filename)
        elif data[0:3] == 'put':
            filename = data.split()[-1]
            ftp.do_put(filename)
        elif data.strip() == 'quit':
            ftp.do_quit()
        else:
            print("请输入正确命令")

if __name__ == "__main__":
    main()








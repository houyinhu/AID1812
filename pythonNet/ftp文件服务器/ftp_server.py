#ftp_server.py
'''
ftp文件服务器
fork server训练
'''

from socket import *
import os,sys
import signal,time

host = '0.0.0.0'
port = 8888
ADDR = (host,port)


#全局变量
FILE_PATH = '/home/tarena/test12/'

class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    
    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        
        files = ''
        for file in file_list:
            if file[0] != '.' \
                and os.path.isfile(FILE_PATH+file):
                files = files + file + ','
        #将拼接号的字符串传给客户端
        self.connfd.send(files.encode())
    
    def do_get(self,filename):
        try :
            fd = open(FILE_PATH+filename,'rb')
        except IOError:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data :
                time.sleep(0.1)
                self.connfd.send(b'#')
                break
            self.connfd.send(data)
    def do_put(self,filename): 
        if os.path.exists(FILE_PATH+filename):
            self.connfd.send('文件已存在'.encode())
            return
        
        f1 = open(FILE_PATH+filename,'wb')
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024)
            if data == b'#':
                break
            f1.write(data)
            f1.flush
        print("保存")



#处理客户端请求
def do_request(connfd):
    while True:
        ftp = FtpServer(connfd)
        data = connfd.recv(1024).decode()
        if data[0] == 'Q' or data is None:
            connfd.close()
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split()[-1]
            ftp.do_get(filename)
        elif data[0] == 'P':
            filename = data.split()[-1]
            ftp.do_put(filename)

#网络搭建
def main():
    sockfd = socket(AF_INET,SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port 8888")
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常：",e)
            continue
        print("连接客户端：",addr)
   
        #创建子进程
        pid = os.fork()  
        if pid == 0:
            sockfd.close()
            do_request(connfd)
            os._exit(0)
        else:
            connfd.close()

if __name__ == '__main__':
    main()    



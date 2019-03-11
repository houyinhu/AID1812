from socket import *
import os,sys
import signal,time
from multiprocessing import Process

host = '0.0.0.0'
port = 8886
ADDR = (host,port)

class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    
    def do_list(self):
        self.connfd.send('OK'.encode())
        time.sleep(0.1)
        filename = ','.join(os.listdir('/home/tarena/test12'))
        self.connfd.send(filename.encode())

    def do_get(self):
        filename = self.connfd.recv(1024).decode()
        try :
            f1 = open('/home/tarena/test12/'+filename,'rb')
            self.connfd.send('OK'.encode())
            time.sleep(0.1)
        except OSError:
            data = '下载文件失败'
            self.connfd.send(data.encode())
        else:
            while True:
                line = f1.read(1024)
                if not line :
                    time.sleep(0.1)
                    self.connfd.send(b'#')
                self.connfd.send(line)
            
    
    def do_put(self):
        data = self.connfd.recv(1024).decode()
        if data in os.listdir('/home/tarena/test12/'):
            self.connfd.send('文件已存在'.encode())
        else:
            self.connfd.send(b'OK')
            f1 = open('/home/tarena/test12/'+data,'wb')
            while True:
                line = self.connfd.recv(1024)
                if line == b'#':
                    break  
                f1.write(line)
                f1.flush()

                
            
#处理客户端请求
def do_request(connfd):
    while True:
        fs = FtpServer(connfd)
        data = connfd.recv(1024).decode()
        if data == 'quit' or not data:
            connfd.close()
            sys.exit('客户端退出')
        elif data == 'list':
            fs.do_list()
        elif data == 'get':
            fs.do_get()
        elif data == 'put':
            fs.do_put()


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close
            sys.exit('服务器退出')
        except Exception:
            print("服务器异常")
            continue
        print("客户端连接:",addr)
        
        pid = os.fork()
        if pid == 0:
            print("创建新进程")
            sockfd.close()
            do_request(connfd)
            sys.exit()
        else:
            connfd.close()

if __name__ == '__main__':
    main()
















from socket import *
from threading import Thread
import sys
class HttpServer(object):
    def __init__(self,addr,file):
        self.addr = addr
        self.file = file
    
    def do_connect(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOCK_STREAM,SO_REUSEADDR,1)
        self.sockfd.bind(self.addr)
        self.sockfd.listen(5)
    def do_request(self):
        self.do_connect()
        while True:
            try:
                connfd,address = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error:",e)
                continue
            else:
                th = Thread(target=self.response,args=(connfd,))
                th.setDaemon(True)
                th.start()


    def response(self,connfd):
        data = connfd.recv(1024).decode()
        if not data:
            return
        data = data.splitlines()
        print(data)
        request = data[0].split(' ')[1]
        print(request)
        if request == "/" or request[-5:] == '.html':
            self.do_response(request,connfd)
        else:
            print("想查看其他网页")
        connfd.close()
    
    def do_response(self,request,connfd):
        if request == '/':
            filename = self.file + '/index.html'
        else:
            filename = self.file + request
        
        try:
            f = open(filename)
        except IOError:
            #没有找到网页
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += '\r\n'
            responseBody = "Sorry,Not found the page"
        else:
            #返回网页内容
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders+='\r\n'
            responseBody = f.read()
        finally:
            response1 = responseHeaders + responseBody
            connfd.send(response1.encode())
def main():
    server_addr = ('0.0.0.0',8888)
    file = './static'
    httpserver = HttpServer(server_addr,file)
    httpserver.do_request()



if __name__ == "__main__":
    main()

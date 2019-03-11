#http2.0_server.py

'''
HTTP Server v2.0
* 多线程并发
* 基本的request解析
* 能够反馈基本数据
* 使用类封装

'''

from socket import *
from threading import Thread
import sys

#封装具体的类作为HTTP server功能模块
class HTTPServer(object):
    def __init__(self,addr,static):
        #添加对象属性
        self.server_addr = addr
        self.static_dir = static
        self.create_socket()
        self.bind()
    
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    
    def bind(self):
        self.sockfd.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Lesten the port %s"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print("Error:",e)
                continue
            #创建多线程处理请求
            clientThread = Thread(target= self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
        
    def handle(self,connfd):
        request = connfd.recv(1024)
        print('request:',request)
        if not request:
            return
        requestHeaders = request.splitlines()
        print('requestHeaders:',requestHeaders)
        print(connfd.getpeername(),':',requestHeaders[0])

        getRequest = str(requestHeaders[0]).split(' ')[1]
        print('getRequest:',getRequest)

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()

    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + getRequest
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
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self,connfd,getRequest):
        responseHeaders = 'HTTP/1.1 200 OK\r\n'
        responseHeaders += '\r\n'
        responseBody = '<p>waiting httpserver v3.0</p>'
        response = responseHeaders + responseBody
        connfd.send(response.encode())




if __name__ == '__main__':
    #使用者自己设定address
    server_addr = ("0.0.0.0",8000)
    #用户提供存放网页的目录
    static_dir = './static'
    #创建服务器对象
    httpd = HTTPServer(server_addr,static_dir)
    #启动服务
    httpd.serve_forever()



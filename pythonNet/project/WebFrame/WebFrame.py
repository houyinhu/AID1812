#!/usr/bin/env python3 
#coding=utf-8
'''
模拟网站后端应用处理程序
httpserver v3.0
'''
from socket import *
from select import select
import json 

# 导入配置文件
from views import *
from settings import *  

# 创建应用类用于具体处理请求
class Application(object):
    def __init__(self):
        self.ip = frame_address[0]
        self.port = frame_address[1]
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(frame_address) 
    
    def start(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        while True:
            rs,ws,xs = select(rlist,wlist,xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = self.sockfd.accept()
                    rlist.append(connfd)
                else:
                    request = connfd.recv(1024).decode()
                    if not request:
                        rlist.remove(r)
                        continue
                    self.handle(r,request)        
    # 处理请求
    def handle(self,connfd,request):
        request = json.loads(request)
        print(request)
        method = request['method']
        path_info = request['path_info']

        if method == 'GET':
            if path_info=='/' or path_info[-5:]=='.html':
                data = self.get_html(path_info)
            else:
                data = self.get_data(path_info)
        elif method == 'POST':
            pass 
        
        connfd.send(data.encode())
       
    
    #处理网页
    def get_html(self,path_info):
        if path_info == '/':
            get_file = STATIC_DIR + "/index.html"
        else:
            get_file = STATIC_DIR + path_info
        try:
            fd = open(get_file)
        except IOError:
            return '404'
        else:
            return fd.read()

    #处理数据
    def get_data(self,path_info):
        for url,func in urls:
            if path_info == url:
                return func()
        return '404'

app = Application()
app.start() #启动后端框架服务

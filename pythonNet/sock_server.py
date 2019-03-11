#sock_server.py

'''
使用socketserver模块完成网络并发模型
'''
from socketserver import * 

#创建tcp多进程并发
class Server(ForkingMixIn,TCPServer):
    pass
# #多线程tcp并发
# class Server(ThreadingMixIn,TCPServer):
#     pass
# class Server(ThreadingTCPServer):
#     pass
#具体请求处理类
class Handler(StreamRequestHandler):
    #重写具体处理方法
    def handle(self):
         print("Connect from:",self.client_address)
         while True:
             #self.request => accept返回的客户端connfd
            data = self.request.recv(1024).decode()
            if not data:
                break
            print(data)
#生成服务器对象
server_addr = ('0.0.0.0',9999)
server = Server(server_addr,Handler)

#启动服务器
server.serve_forever()






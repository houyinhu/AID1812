#http_server.py
'''
http server v1.0
接受浏览器请求
返回固定的相应内容
'''
from socket import *

#处理客户端请求
def handleClient(connfd):
    print("Request from",connfd.getpeername())
    request = connfd.recv(1024)#接受http请求
    #将request按行分割
    request_lines = request.splitlines()
    for line in request_lines:
        print(line)
    
    try:
        f = open('index.html')
    except IOError as c:
        response = "HTTP/1.1 404 Not Found\r\n"
        response+="\r\n"
        response+="==Sorry"
    else:
        response = "HTTP/1.1 200 ok"
        response+="\r\n"
        response+=f.read()
    finally:
        #将结果发送给浏览器
        connfd.send(response.encode())

#创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print("listen to the poet 8000")
    print(sockfd.getpeername)
    while True:
        connfd,addr = sockfd.accept()
        handleClient(connfd)#负责具体请求处理
        connfd.close()

if __name__ == "__main__":

    main()




from socket import *

s = socket()
#对套接字设置为立即重用端口
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

print(s.family) #地址类型
print(s.type)   #套接字类型

s.bind(('0.0.0.1',8888))
print(s.getsockname())#获取绑定的addr
print(s.fileno())   #获取文件描述符

s.listen(3)
c,addr = s.accept()

print(c.getpeername())


IO句柄
stdout.fileno()
stderr.fileno()
stdin.fileno()
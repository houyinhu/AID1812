#file_server.py

from socket import * 

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(('0.0.0.0',8888))

sockfd.listen(5)

print("等待连接")
connfd,addr = sockfd.accept()

while True:

    data = connfd.recv(1024)
    dataline = data.decode()
    if not data:
        break
    try:
        f = open('a2.txt','wt',encoding='utf8')
        f.write(dataline)
    except :
        print("保存文件失败")
    finally:
        f.close()
    print("来自%s的消息：%s"%(addr,data.decode()))
    
    data = '收到消息'
    connfd.send(data.encode())

connfd.close()
sockfd.close()











#dictionary_server.py
import pymysql
from socket import *
from multiprocessing import Process
import os,sys,signal,time

#处理注册事件
def do_re(c,db):
    c.send(b'OK')
    np = c.recv(1024).decode()
    if not np or np == '#':
        return
    nameword = np.split(' ')
    name = nameword[0]
    passwd = nameword[1]
    #判断姓名是否存在
    sql = "select * from user where name = '%s'"%name
    #创建游标
    cursor = db.cursor()
    #执行sql语句
    cursor.execute(sql)
    r = cursor.fetchone()
    print(r)
    if r != None:
        c.send("not".encode())
    else:  
        #插入姓名，密码
        sql = "insert into user values(null,'%s','%s');"%(name,passwd)
        cursor.execute(sql)
        db.commit()
        c.send('ok'.encode())
        return
    cursor.close()

def do_in(c,db):
    while True:
        np = c.recv(1024).decode()
        namewd = np.split(' ')
        name = namewd[0]
        passwd = namewd[1]
        print('name:',name,passwd)
        sql = "select * from user where name = '%s' and passwd = '%s'"%(name,passwd)
        #创建游标
        cursor = db.cursor()
        #执行sql语句
        cursor.execute(sql)
        r = cursor.fetchone()
        print("r:",r)
        if r != None:
            c.send(b"ok")
            break
        else :
            c.send("not".encode())
    
    while True:
        data = c.recv(1024).decode()
        if not data:
            return
        elif data == 'H':
            do_hist(c,db)
        elif data == 'Q':
            do_query(c,db,name)
        elif data == '#':
            break

def do_hist(c,db):
    print("开始")
    cursor = db.cursor()
    sql = "select * from history order by id desc limit 10;"
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        time.sleep(0.1)
        msg = i[1]+' '+i[2] + ' '+ i[3]
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'#')



def do_query(c,db,name):
    print("查询")
    cursor = db.cursor()
    while True:
        query = c.recv(1024).decode()
        if query == '#':
            return
        sql="select * from words where word = '%s';"%query
        cursor.execute(sql)
        r = cursor.fetchone() 
        if r != None:
            query1 = r[1]+' :'+r[2]
            print(query1)
            c.send(query1.encode()) 
        else:
            print("执行嗯了")
            c.send(b'#')
        sql = "insert into history values(null,'%s','%s','%s');"%(name,query,time.ctime())
        cursor.execute(sql)
        db.commit()

        

#处理请求
def do_request(c,db):
    while True:
        data = c.recv(1024).decode()
        if not data:
            return
        elif data == 'I':
            do_in(c,db)
        elif data == 'R':
            do_re(c,db)

def main():
    #连接数据库
    db = pymysql.connect('localhost','root','123456','dict')
    sockfd = socket()
    sockfd.setsockopt(SOCK_STREAM,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8888))
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr = sockfd.accept()
            print("来自客户端：",addr)
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("Error:",e)

        pid = os.fork()
        if pid == 0:
            sockfd.close()
            do_request(c,db)
            sys.exit("谢谢使用")
        else:
            c.close()



if __name__ == '__main__':
    main()



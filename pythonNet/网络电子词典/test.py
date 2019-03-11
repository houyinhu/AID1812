import pymysql

def mysq():
    host = 'localhost' #服务器地址
    user = 'root'   #用户名
    passwd = '123456'   #密码
    dbname = 'dict'     #库名称
    # - 建立数据库连接
    conn = pymysql.connect(host,user,passwd,dbname)
    # - 获取游标对象
    cursor1 = conn.cursor()
    
    # - 使用游标对象提供的方法，执行SQL语句

    try:
        f1 = open('dict.txt','rt') 
    except OSError:
        print("打开文件失败")
    else:
        while True:
            line = f1.readline()
            if not line:
                break
            f1list = line.split()
            xname = f1list[0]
            xexplain = ''.join(f1list[1:])
            try:
                insert = "insert into words values(null,'%s','%s');"%(xname,xexplain)
                cursor1.execute(insert)
            except:
                continue
        #提交事务
        conn.commit()
    # 关闭游标
    cursor1.close()
    #关闭数据库链接
    conn.close()
mysq()
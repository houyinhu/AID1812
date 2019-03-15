#update.py

import pymysql
from db_conf import *

try:
    #连接数据库
    conn = pymysql.connect(host,user,passwd,dbname)
    # 获取游标
    c = conn.cursor()
    # 执行SQL语句
    a = input("请输入")
    sql = '''
    update acct set balance = balance + 100 
    where acct_no = '622345000008'
    '''
    c.execute(sql)#执行插入
    conn.commit()   #提交事务
    c.close()  #关闭游标
    print("修改成功,影响笔数：%d" % c.rowcount)

except Exception as e:
    conn.rollback() #出现异常回滚事务
    print("数据库操作失败")
    print(e)
finally:
    print("asdf")
    conn.close()#关闭连接
class A():
    def __init__(self):
        db = db_conf.connect()
        course = db.course()










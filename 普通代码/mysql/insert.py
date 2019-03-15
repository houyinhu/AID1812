
# insert.py
# 插入示例
import pymysql
from db_conf import *

try:
    #连接数据库
    conn = pymysql.connect(host,user,passwd,dbname)
    # 获取游标
    c = conn.cursor()
    # 执行SQL语句
    sql = "insert into acct values('6223450000009','robert','c0008',1,date(now()),1,555.3)"
    c.execute(sql)#执行插入
    conn.commit()   #提交事务
    c.close()  #关闭游标

except Exception as e:
    conn.rollback() #出现异常回滚事务
    print("数据库操作失败")
    print(e)
finally:
    print("asdf")
    conn.close()#关闭连接




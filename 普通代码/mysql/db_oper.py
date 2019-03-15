#db_oper.py
import pymysql
import db_conf

class DBOper:
    def __init__(self): #构造方法
        self.host = db_conf.host
        self.user = db_conf.user
        self.passwd = db_conf.passwd
        self.dbname = db_conf.dbname
        self.db_conn = None  #数据库连接对象

    def open_conn(self): #连接数据库
        try:
            self.db_conn = pymysql.connect(
                self.host, self.user, 
                self.passwd, self.dbname)
        except Exception as e:
            print("数据库连接错误")
            print(e)
        else:
            print("数据库连接成功")

    def close_conn(self):#关闭连接
        try:
            self.db_conn.close()
        except Exception as e:
            print("数据库关闭错误")
            print(e)
        else:
            print("数据库关闭成功")

    # 执行查询, 返回结果集
    def do_query(self, sql): 
        if not sql:  #参数合法性判断
            print("SQL语句不合法")
            return None 
        if sql == "": #参数合法性判断
            print("SQL语句不合法")
            return None 
        try:
            cursor = self.db_conn.cursor()#获取游标
            cursor.execute(sql) #执行sql语句
            result = cursor.fetchall() #获取数据
            cursor.close() #关闭游标
            return result  #返回查询数据集 
        except Exception as e:
            print("查询出错")
            print(e)
            return None

    # 执行增、删、改等变更操作           
    def do_update(self, sql): 
        if not sql:  #参数合法性判断
            print("SQL语句不合法")
            return None 

        if sql == "": #参数合法性判断
            print("SQL语句不合法")
            return None 

        try:
            cursor = self.db_conn.cursor()#获取游标
            result = cursor.execute(sql)#执行SQL语句
            self.db_conn.commit()  #提交事务
            cursor.close()
            return result  #返回受影响的笔数
        except Exception as e:
            print("执行SQL语句出错")
            print(e)
            return None













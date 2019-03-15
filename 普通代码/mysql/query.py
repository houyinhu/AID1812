# query.py
# pymysql查询示例

# - 导入pymysql模块
# - 建立数据库连接
# - 获取游标对象
# - 使用游标对象提供的方法，执行SQL语句
# - 提交事务（如果需要）
# - 关闭数据库连接对象


# - 导入pymysql模块
import pymysql
host = 'localhost' #服务器地址
user = 'root'   #用户名
passwd = '123456'   #密码
dbname = 'bank'     #库名称
# - 建立数据库连接
conn = pymysql.connect(host,user,passwd,dbname)
# - 获取游标对象
cursor1 = conn.cursor()
# - 使用游标对象提供的方法，执行SQL语句
cursor1.execute("select * from acct")
result = cursor1.fetchall()  #取查到的数据
print(result)
print("查询完成")
print(type(result))
for r in result:    #遍历结果集，取字段，打印
    tmp = "帐号：%s,户名：%s,金额：%s"%(r[0],r[1],r[6])
    print(tmp)
# 关闭游标
cursor1.close()
#关闭数据库链接
conn.close()

#mongo.py
from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#生成数据库对象
db = conn.stu

#创建集合对象
myset = db.class4

#数据操作

#插入操作
# myset.insert_one({'name':'张贴林','King':'乾隆'})
# myset.insert_many([{'name':'张国立','King':'康熙'},\
    # {'name':'陈道明','King':'康熙'}])
# myset.insert({'name':'唐国强','King':'雍正'})
# myset.insert([{'name':'陈建斌','King':'雍正'},\
#     {'_id':1,'name':'吴奇隆','King':'四爷'}])
# myset.save({'_id':1,'name':'捏远','King':'乾隆'})

#查找操作
#*************find*********************
# cursor = myset.find({'name':{'$exists':True}},{'_id':0})

# for i in cursor:
#     print(i['name'],':',i['King'])

# print(cursor.next()) #下面会报错
#取前三条
# for i in cursor.sort([('name',1),('age',-1)]).limit(3):
#     print(i)

# dic = {'$or':[{'King':'乾隆'},{'name':'陈道明'}]}
# d = myset.find_one(dic)
# print(d)

#***************update******************
# myset.update_many({'King':'康熙'},{'$set':{'king_name':'玄也'}})

# myset.update_one({'name':'郑少秋'},{'$set':{'King':'乾隆'}},upsert=True)

# myset.update({'King':'乾隆'},{'$set':{'King_name':'红利'}},multi=True)

#******************delete************
# myset.delete_one({'King':'康熙'})
# myset.delete_many({'King':'雍正'})
# myset.remove({'king_name':{'$exists':False}},multi=True)
# myset.remove({'king_name':None)

#***************复合操作************
# data = myset.find_one_and_delete({'King':'康熙'})
# print(data)





#关闭连接
conn.close()
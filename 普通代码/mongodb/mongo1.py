from pymongo import MongoClient
conn = MongoClient('localhost',27017)

db = conn.stu
myset = db.class0

#索引聚合
#×××××××××××××××××××索引××××××××××××××××
#创建索引
# index_name = myset.create_index('name')
index_name = myset.create_index([('name',1)])
# index_age = myset.create_index('age',name='Age',sparse=True)


# myset.drop_index('Age')#删除Age索引
myset.drop_index([('name',1)])#也可以通过键值对删除
# myset.drop_indexes()    #删除所有索引

#查看索引
for i in myset.list_indexes():
    print(i)

#××××××××××××××××××××聚合×××××××××××××8
# l = [
#     {'$group':{'_id':'$sex','num':{'$sum':1}}}
# ]

# cursor = myset.aggregate(l)
# for i in cursor:
#     print(i)


conn.close()



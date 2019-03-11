

l=[]#创建一个列表，准备存放学生数据的字典
while True:
    name=input("请输入姓名")
    if name == '':#如果用户输入空字符串就结束输入
        break
    age=(input("请输入年龄"))
    if age == '':
        break
    score=(input("请输入成绩"))
    if score == '':
        break
    d={}#创建一个空字典，用来接受信息
    d['name']=name
    d['age']=age
    d['score']=score
    l+=[d]
print(l)

print("+",' ')
print("+------------------+----------------+------------+")
print("|       姓名       |      年龄      |    成绩    |")
print("+------------------+----------------+------------+")
for d in l:
    name=d['name']
    age=str(d['age'])
    score=str (d['score'])
    print("|%s|%s|%s|"%(name.center(18),
                        age.center(16),
                        score.center(12)),
                        )
# |         tarena   |          20       |       99     |
# |         name2    |          18       |       88     |
print("+------------------+----------------+------------+")


# print('姓名'.center(18)+'年龄'.center(15)+'成绩'.center(11))
# for x in l:
#     print(x['name'].center(20)+x['age'].center(15)+x['score'].center(15))


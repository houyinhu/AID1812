
def add_information(L):
    #添加学生信息
    while True:
        name = input("请输入姓名")
        if name == '':  # 如果用户输入空字符串就结束输入
            break
        age = int(input("请输入年龄"))
        if age == '':
            break
        score = int(input("请输入成绩"))
        if score == '':
            break
        d = {}  # 创建一个空字典，用来接受信息
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)

def output_student(L):
    #显示学生信息
    print("+------------------+----------------+------------+")
    print("|       姓名       |      年龄      |    成绩    |")
    print("+------------------+----------------+------------+")

    for d in L:
        count = 0  # 用来记录名字中 出现中文的个数
        name = d['name']
        age = str(d['age'])
        score = str(d['score'])
        for x in name:
            if 0x4E00 < ord(x) < 0x9FA5:
                count+=1
        print("|%s|%s|%s|" % (name.center(18-count),
                              age.center(16),
                              score.center(12)),
              )
    print("+------------------+----------------+------------+")

def delete_student(L):
    #删除学生信息
    x=input("请选择你要删除的学生信息")
    for i in L:
        if i['name'] == x:
            L.remove(i)
            print("删除成功")
        else:
            print('删除失败请从新操作')

def modify_score(L):
    #修改学生成绩
    a=input("请选择要修改成绩的学生")
    score1=int(input("请输入要修改的分数"))
    for x in L:
        if x['name']==a:
            x['score']=score1
            print("找不到要修改的学生")

def scoresheng(L):
    def d(x):
        return x['score']
    a = sorted(L, key=d)
    output_student(a)

def scorejiang(L):
    def d(x):
        return x['score']
    a = sorted(L, key=d, reverse=True)
    output_student(a)
def agesheng(L):
    # def d(x):
    #     return x['age']
    a=sorted(L, key=lambda x:x['score'])
    output_student(a)
def agejiang(L):
    def d(x):
        return x['age']
    a=sorted(L, key=d,reverse=True)
    output_student(a)












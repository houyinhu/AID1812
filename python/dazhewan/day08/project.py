


def input_student():
    l = []  # 创建一个列表，准备存放学生数据的字典
    while True:
        name = input("请输入姓名")
        if name == '':  # 如果用户输入空字符串就结束输入
            break
        age = (input("请输入年龄"))
        if age == '':
            break
        score = (input("请输入成绩"))
        if score == '':
            break
        d = {}  # 创建一个空字典，用来接受信息
        d['name'] = name
        d['age'] = age
        d['score'] = score
        l += [d]
    return l
def output_student(l):
    print("+------------------+----------------+------------+")
    print("|       姓名       |      年龄      |    成绩    |")
    print("+------------------+----------------+------------+")

    for d in l:
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

infos=input_student()
print(infos)	#打印列表[{..},{...}]
output_student(infos)#根据实参infos打印表格




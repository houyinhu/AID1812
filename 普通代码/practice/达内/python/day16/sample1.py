
# 写一个函数，要求把一个字典组成的列表（学生信息列表）
# ，写入文件si.txt中
# 要求：
# 内容是每个学生的信息写在一行内，每个信息之间用逗号分隔开
def save_to_file(L):
    try:
        f = open('si.txt','w',encoding='utf-8')
        #循环写入每个学生的信息
        for x in L:
            f.write('%s,%s,%s'%(x['name'],x['age'],x['score']))
            f.write('\n')
        f.close()
    except  OSError:
        print("打开文件错误")
    except:
        print('有错误')

L = [dict(name='xiaozhang',age=20,score=90),
     dict(name='xiaoli', age=18, score=98),
     ]
save_to_file(L)







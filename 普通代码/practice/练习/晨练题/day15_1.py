

# 练习1：
# 现有一个列表alist= ['hello','world']，写一个程序要求实现如下输出：
# index 0：hello
# index 1：world


# alist= ['hello','world']
#
# for x,y in enumerate(alist):
#     print("index%s:%s"%(x,y))




# 练习2：
# 写一个程序，要求实现如下功能：
# (1). 创建一个文件student_info.txt
# (2). 在文件中写入如下两行内容：
# 	name:Bob  age:30  score: 90
# 	name:Lucy age:25  score: 99
#
# a = open('student_info.txt','w',encoding='utf-8')
# a.write("name:Bob  age:30  score: 90\n")
# a.write("name:Lucy age:25  score: 99")
# a.close()



# 练习3：
# 写一个生成器函数myyield()，将练习2中student_info.txt中的两行内容生成一个生成器
# 然后用for语句打印这两行内容：


def myyield():
    try:
        f1 = open('student_info.txt',encoding='utf-8')
        while True:
            a = f1.readline()
            if not a:
                break
            yield a
    except OSError:
        print("打开文件错误")
    finally:
        f1.close()

for x in myyield():
    print(x)

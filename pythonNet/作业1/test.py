
#计算密集型 x,y传入1
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1
# 单进程执行10遍
# 创建10个多线程执行1边
# 创建10个多进程执行1边

#io 密集

def write():
    f = open("text",'w')
    for i in range(1200000):
        f.write("hello workd\n")
    f.close()

def read():
    f = open("text")
    lines = f.readlines()
    f.close()
# 单进程执行10遍
# 创建10个多线程执行1边
# 创建10个多进程执行1边
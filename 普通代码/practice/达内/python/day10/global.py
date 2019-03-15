
# v=100
# def f1():
#     global v        #全局声明语句
#     v=200
# f1()
# print(v)

#
# v=100
# def fx():
#     v=200
#     global v    #不能先声明局部变量，再用global声明为全局变量，此做法不符合规则
#     v+=300
#     print(v)
# fx()
# print(v)

# v=100
# def fx(v):
#     print(v)
#     # global v
#     v=300
#
# fx(200)
# print(v)

#用全局变量记录一个函数fx调用的次数，部分代码如下：
count = 0
def fx(name):
    print("你好",name)
    global count
    count+=1

fx('小张')
fx("小李")
print("fx函数共被调用",count,'次')

















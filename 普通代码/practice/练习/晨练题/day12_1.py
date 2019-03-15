
# 练习1：
# 写一个函数myfn(n)，要求：
# (1). 每隔1秒在屏幕打印"hello world"，共打印n次
# (2). 请在函数中加入文档字符串：
# """myfn函数是输出n遍"hello world"
#     n为参数
# """
# (3). 优先用递归方法完成此函数(也可以用while循环)

import time
def myfn(n):
    if n >0:
        print('hello world')
        time.sleep(1)
    if n<=0:
        return

    return myfn(n-1)

n=int(input("请输入要打印的次数"))
myfn(n)


# import time
# def myfn(n):
#     '''myfn函数式输出n遍Hello World'''
#     for x in range(n):
#         print('hello world')
#         time.sleep(1)
#
#
# n=int(input("请输入要打印的次数"))
# myfn(n)





# 练习2：
# 在练习1中的函数外部加入如下语句：
a = myfn
print(a.__name__)
print(myfn.__name__)
# 请问输出结果是什么？代表什么意思？









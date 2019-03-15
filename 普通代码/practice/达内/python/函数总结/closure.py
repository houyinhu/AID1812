
#闭包
def make_pow(y):
    def pow(x):
        return x**y
    return pow
a=make_pow(2)
print(a(3))


# #装饰器
# def 装饰器函数名():
#     语句块
#     return 函数对象
#
# @装饰器函数名
# def 被装饰函数名(形参列表)：
#     语句块
#     -------------------------------------
def mydeco(fn):
    def fx():
        print("+++这是myfunc被调用之前++++")
        fn()
        print("+++这是myfunc被调用之后++++")
    return fx
@mydeco
def myfunc():
    print("myfunc被调用")






def make_except():
    print("函数开始...")
    error = ValueError("这是故意制造的错误！！")   #构造函数 对象
    raise error


    print("函数接受")

try:
    make_except()
    print("make_except 调用完毕！")
except ZeroDivisionError:
    print("make_except 函数调用发生异常")
except ValueError as err:       # as 子句是用于绑定错误对象的变量
    print("发生了值错误！！",err)

print("程序正常退出！")














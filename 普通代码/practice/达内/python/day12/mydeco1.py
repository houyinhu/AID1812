

#此示例示意装饰器的原理和语法
def mydeco(fn):
    def fx():
        print("+++++++++++++++++")
        fn()
        print("-----------------")
    return fx

def myfunc():
    #被装饰函数
    print("函数myfunc被调用")

myfunc = mydeco(myfunc)
myfunc()
myfunc()
myfunc()
















#此示例示意装饰器的原理和语法
def mydeco(fn):
    def fx():
        print("+++++++++++++++++")
        fn()
        print("-----------------")
    return fx
@mydeco     #  @mydeco等同于 myfunc = mydeco(myfunc)
# myfunc = mydeco(myfunc)
def myfunc():
    #被装饰函数
    print("函数myfunc被调用")


myfunc()
























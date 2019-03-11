

#此示例示意__all__列表在模块中的应用
#__all__列表只能影响from import*语句，其他语句不受限制
__all__=['f1','name1']

def f1():
    f2()
    f3()
    pass
def f2():
    pass
def f3():
    pass
name1='aaa'
name2='bbb'









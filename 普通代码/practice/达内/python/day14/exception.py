
def f1():
    err = ValueError("一个错误")

    pass

def f2():
    f1()

def f3():
    f2()

def f4():
    f3()

try:
    f4()
except ValueError as err:
    print(err)











# def f1():
#     err = ValueError("一个错误")
#     print("你好帅")
#     return err
#     pass
#
# def f2():
#     f1()
#     return f1()
#
# def f3():
#     f2()
#     return f2()
#
# def f4():
#     f3()
#     return f3()
# e = f4()















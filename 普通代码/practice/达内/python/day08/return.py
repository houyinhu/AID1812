
# def say_hello():
#     print("hello aaa")
#     print("hello bbb")
#     print("hello ccc")
#     return None
# v=say_hello()
# print("v=",v)


def mymax(a,b):
    '''
    方法一
    zuida = a
    if b> zuida:
        zuida=b
    return zuida
    '''
    # 方法2
    # if a>b:
    #     return a
    # else:
    #     return b
    return max(a,b)
print(mymax(100,200))
print(mymax("abc",'abcd'))









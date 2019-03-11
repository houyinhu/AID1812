
# L=[1,2,3]
# def f(n=0,lst=[]):
#     '''缺省参数[]在def语句执行时就已经创建该列表，并一直被f函数绑定'''
#     lst.append(n)
#     print(lst)
# f(4,L)
# f(5,L)
# f(100)
# print(id(f(100)))
# f(200)
# print(id(f(200)))

#解决办法：
L=[1,2,3]
def f(n=0,lst=None):
    if lst is None:
        lst=[]#创建一个新列表
    lst.append(n)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)







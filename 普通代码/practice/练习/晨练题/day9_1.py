# 练习1：现有如下函数：
# def myfun(x):
#     if  x > 0:
#         print  (x,"是正数")
#         return x
#     else:
#         return  x
#         print (x,"是负数或者0")


def myfun1(a,b,c):
    print(a,b,c)
# 请分别用四种方式给其传参(1传给a,2传给b,3传给c)：位置传参、序列传参、关键字传参、字典关键字传参

# # myfun1(1,2,3)
# l=(1,2,3)
# myfun1(*l)
# # myfun1(a=1,b=2,c=3)
d={'a':1,'b':2,'c':3}
myfun1(**d)


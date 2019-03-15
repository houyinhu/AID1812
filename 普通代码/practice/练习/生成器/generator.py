

# 生辰器是能够动态提供数据的对象，生成器对象也是可迭代对象
# 生成器实在程序运行时生成的数据，与容器类不同
#
#
# 含有yield语句的函数是生成器函数
# yield语句只能用于def函数中，母的是将此函数作为生成器函数使用
# def myyield():
#     #此函数调用固定生成2357四个数
#     yield 2
#     yield 3
#     yield 5
#     yield 7
# for x in myyield():#调用生成器函数，返回可迭代的生成器对象
#     print(x)

# def myinteger(n):
#     i=0
#     while i < n:
#         yield i
#         i+=1
# 生成器函数每次运行到yield语句则暂停执行，保存此函数当前的执行状态，
# 下一次调用next(it)时则从当前的执行状态开始继续执行
# for x in myinteger(3):
#     print(x)
# it = iter(myinteger(2))
# print(next(it))
# print(next(it))
# print(next(it))


# def myyield():
#     print("即将生成2")
#     yield 2
#     print("即将生成3")
#     yield 3
#     print("即将生成5")
#     yield 5
#     print("生成结束")
#
# it = iter(myyield())
# next(it)
# next(it)
# next(it)
# next(it)


# def myodd(y):
#     x=0
#     while x<=y:
#         if x %2 ==1 :
#             print(x)
#             yield
#         x+=1
# for x in myodd(5):
#     print(x)

# it=iter(myodd(5))
# next(it)
# next(it)
# next(it)


# def myprimes(n):
#     x=3
#     while x<=n:
#         for y in range(2,x):
#             if x % y ==0:
#                 break
#         else:
#             yield x
#         x+=1
# it =iter(myprimes(10))
# print(next(it))
# print(next(it))
# print(next(it))
# for x in myprimes(10):
#     print(x)

# 生成器表达式
for x in (x for x in range(1,10)  if x%2!=0):
    print(x)



# 已知有列表：
# L=[2,3,5,7]
# 1,写一个生成器函数，让此函数能够动态提供数据，数据为原列表的平方加1
# 2，写一个生成器表达式，让此表达式能够动态提供数据，数据位元列表的数的
# 的平方加1
# 3，创建一个列表，让此列表内的数据为原数据的平方加1

L=[2,3,5,7]
def ping(L1):
    for x in L1:
        yield x**2+1
it = iter(ping(L))
print(next(it))
print(next(it))

# L=[2,3,5,7]
# # biao = (x**2+1 for x in L)
# # it1 = iter(biao)
# # print(next(it1))
#
#
# l1=list(x**2+1 for x in L)
# print(l1)

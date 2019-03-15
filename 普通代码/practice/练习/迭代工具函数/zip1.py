
# 返回一个zip生成器对象，此对象用于生成一个元组，此元组的数据分别来自于
# 参数中每个科迭代对象，生成元组的个数有最小的可迭代对象大小决定


L=list(zip("abcd",range(1,20)))
for x in L:
    print(x)
print(L)

# for x in zip("avc",'1234'):
#     print(x)















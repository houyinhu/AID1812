

# 1,将1~20的数用filter 生成能够提供偶数的可迭代对象，生成1~20的偶数，
# 将这些偶数存于列表中，在打印这个列表（不包含20）

#方法一
# for x in filter(lambda x : x%2==0,range(20)):
#     print(x)
#方法二
# flt=filter(lambda x: x%2==0,range(1,20))
# L=list(flt)
# print("L1=",L)
#方法三
# L2=[x for x in filter(lambda x: x%2==0,range(1,20))]
# print("L2=",L2)

# 2,用filter函数，将1~100之间所有的素数prime放入到列表中，
# 在打印这个列表

#写一个函数，is_prime(x),判断如果x是素数返回True，否则返回False
# def is_prime(x):
#     if x <2:    #小于2的数没有素数
#         return False
#     #大于等于2的数，如果能被2-x-1整数就不是素数
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     #走到此处，则一定是素数
#     return True
#方法一
# l1=list(filter(is_prime,range(1,101)))
# print("l1=",l1)

#方法二
# l2=[x for x in filter(is_prime,range(1,100))]
# print("l2=",l2)

#方法三
# l3=[x for x in range(100) if is_prime(x)]
# print("l3=",l3)










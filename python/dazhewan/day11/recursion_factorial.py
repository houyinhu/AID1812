
# def myfac(n):
#     if  n == 0:
#         return 1
#     else:
#         return n * myfac(n-1)
# print(myfac(5))
#
# 此函数求1+2+3+4+5+6+...+n

#写一个递归函数求和：
# def mysum(n):
#     if  n==1:
#         return 1
#     else:
#         return n + mysum(n-1)
# print(mysum(100))

def f1(n):
    if n ==1:
        return 10
    return f1(n-1)+2
print(f1(5))
print(f1(3))

# def age(n):
#     if n == 1: c = 10
#     else: c = age(n - 1) + 2
#     return c
# print(age(5))


# def get_age(n):
#     if n ==1:
#         return 10
#     return get_age(n+1)+2
# get_age(1)











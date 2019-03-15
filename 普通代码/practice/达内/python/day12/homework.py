# 1，编写函数fun，其功能室计算并返回下列多项式的和
# Sn = 1 + 1/ 1！+1 / 2!+1 / 3!+....1 / n!
#方法二
# def Sn(n):
#     def jc(n):
#         if n == 1:
#             return 1
#         else:
#             return n * jc(n - 1)
#     for x in range(n):
#         if x ==0:
#             sum1=1
#         else:
#             sum1+=jc(x)**-1
#     return sum1

# def fun(n):
#     from math import  factorial as fac
#     return sum([1/fac(x) for x in range(n+1)])


#方法三
def fun(n):
    from math import factorial as fac
    return  sum(map(lambda x:1/fac(x),range(n+1)))

print(fun(20))



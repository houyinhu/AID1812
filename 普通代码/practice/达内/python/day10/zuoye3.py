

# def myfac(n):
#     sum1=0
#     for x in range(1,n+1):
#         sum1+=x**x
#     return sum1
# print(myfac(3))

#方法二
# def mysum(n):
#     s = sum([x**x for x in range(1,n+1)])
#     return s
# print(mysum(3))

#方法三
def mysum(n):
    return sum(map(lambda x : x**x,range(1,n+1)))
print(mysum(3))












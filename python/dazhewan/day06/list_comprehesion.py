# 生成一个数值为1~9的整数的平方的列表，如：
# L=[1,4,9,16,25,36,49,64,81]
# 循环语句
# l=[]
# for x in range(1,10):
#     l.append(x**2)
# print(l)
'''
# 列表推导
l=[x**2 for x in range(1,10)]
print("l:",l)
'''
l1=[x for x in range(1,100,2)]
print(l1)
l2=[x for x in range(1,100) if x%2==1]
print(l2)
l3=[]
for x in range(1,100):
    if x%2==1:   
        l3.append(x)
print(l3)



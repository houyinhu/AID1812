
# 练习1：
# a = 100
# b = 200
# s = input("请输入字符串 a+b： ")
# m = eval(s)
# n = exec(s)
# print(m)
# print(n)
# 请问 m和n的值分别是什么？ 掌握eval()和exec()函数的用法

# 练习2：
L1 = [x for x in map(lambda x,y: x+y,[1,2,3,4],[5,6,8])]
print(L1)
# 请问L1的值是什么？
# (2).用filter()函数筛选L1中的奇数
a=filter(lambda x:x%2==1,L1)
for x in a:
    print(x)


# 练习3：
D = [{"name": "Green","age": 30},{"name": "Bob","age":25}]
# 请用sorted()函数按年龄从低到高排列列表中的元素

a = sorted(D,key=lambda x:x['age'],reverse=True)
print(a)











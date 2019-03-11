# 生成一个1~0平方的元组，元组如下：
# （1,4,9,16，。。。81）

#方法一
t=()
for x in range(1,10):
    t+=(x**2,)
print(t)

#方法二
l=[x**2 for x in range(1,10)]
t=tuple(l)
print(t)

#方法三
t=tuple(x**2 for x in range(1,10))
print(t)

#方法四
g=(x**2 for x in range(1,10))
t=tuple(g)
print(g)

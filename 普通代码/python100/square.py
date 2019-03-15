#题目：求输入数字的平方，如果平方运算后小于 50 则退出。

def s1(a):
    return a**2
while True:
    num1 = int(input("请输入数字"))
    s2 = s1(num1)
    print("%s的平方式：%s"%(num1,s2))
    if s2 < 50:
        break

f1 = lambda a:a**2
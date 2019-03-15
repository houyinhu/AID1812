
# 求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    i1 = int(input("请输入一个数字"))
    if i1**2 <50:
        print('平方小于50，退出程序')
        break
    else:
        print("%s的平方是：%s"%(i1,i1**2))












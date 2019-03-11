
# 练习:
#   1. 猜数字游戏
#     随机生成一个 0~100之间的一个整数，用变量x绑定
#     让用户输入一个数y,输出猜数字的结果:
#       1) 如果y大于x则提示: "您猜大了"
#       2) 如果y小于x则提示: "您猜小了"
#       3) 如果y等于生成的数x,则提供示用户"恭喜您猜对了 "并退出猜数字
#     循环重复上述步聚，直到猜对为止。
#     猜对了，显示用户猜数字的次数，然后退出程序

import random
x=random.randint(1,100)
n=1
while True:
    try:
        y=int(input("请输入0-100内的一个整数："))
    except :
        print("你输入错误")
        continue
    if y>x:
        print("你猜大了")
    if y<x:
        print("你猜小了")
    if y == x :
        print("恭喜你猜对了","你总共用了%s次"%(n))
        break
    n+=1












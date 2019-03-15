

# 10-7 加法计算器：将你为完成练习 10-6 而编写的代码放在一个 while 循环
# 中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字

while   True:
    def sum1():
        print("下面是两个数的加法运算")
        num1 = 0
        n1 = int(input("请输入第一个数字"))
        n2 = int(input("请输入第二个数字"))
        num1 = n1 + n2
        print(num1)

    try:
        sum1()
    except ValueError:
        print("你输入有错")
    else:
        break












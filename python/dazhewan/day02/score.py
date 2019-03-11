# 2. 输入一个学生的三科成绩(三个整数):
#     打印出最高分是多少？
#     打印出最低分是多少？
#     打印出平均分是多少？
x=int(input("请输入第一个成绩"))
y=int(input("请输入第二个成绩"))
z=int(input("请输入第三个成绩"))
if x<y:
    if y<z:
        da=z
    elif y>z:
        da=y
elif x>y:
    if x<z:
        da=z
    elif  x>z:
        da=x
ping=(x+y+z)/3
print("最大值为",da)
print("平均值为",ping)
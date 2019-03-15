# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。
# 程序源代码：
n=int(input("请输入几个数相加"))
n2=int(input("请输入相同的数字"))
s=0
for i in range(1,n+1):
    for j in range(0,i):
        s+=n2*10**j
print(s)
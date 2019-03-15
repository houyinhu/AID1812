# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义
num1=int(input("请输入斐波那契数列长度"))
a=[0,1]
n=2
num2=0
while n<num1 :
    num2=a[n-1]+a[n-2]
    a.append(num2)
    n+=1
print(a)


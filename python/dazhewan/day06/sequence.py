# 1.写程序，让用户循环输入一些正整数，当输入-1时结束输入，将这些
# 整数存于列表l中 
# 1）打印出你共输入了几个有效的数（不算结束的-1）
# 2）打印你输入的最大数是多少？
# 3）打印您输入的最小数是多少
# 4）打印你输入的这些书的平均值是多少


n1=0    #记录输入了几个有效数字
l=[]  #创建一个列表容器，准备存放数据
while True:
    count=int(input("请输入正整数"))
    if count<0:
        break
    l+=[count]
    n1+=1
print("你一共输入了%d个有效的数"%n1)
print("你输入的最大数是%d"%max(l))
print("你输入的最小数是%d"%min(l))
print("这些数的平均值是",sum(l)/n1)
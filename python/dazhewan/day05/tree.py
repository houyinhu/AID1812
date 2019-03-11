1.输入一个整数，代表树干的高度，打印如下一课”圣诞树：
如 ：
请输入：2
num1=int(input("请输入树干的高度"))
count=2*num1-1#代表最长的树叶
for i in range(1,num1+1):
    print(('*'*(2*i-1)).center(count))
for j in range(1,num1+1):
    print('*'.center(count))


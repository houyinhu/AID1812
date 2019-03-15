# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

num1=int(input("请输入第一个整数"))
num2=int(input("请输入第二个整数"))
num3=int(input("请输入第三个整数"))

# num=[num1,num2,num3]
# num4=sorted(num)
# print("从小到大排列",num4)

max1=max(num1,num2,num3)
min1=min(num1,num2,num3)
zhong=0
if num1!=max1 and num1!=min1:
    zhong=num1
elif num2!=max1 and num2!=min1:
    zhong=num2
else:
    zhong=num3
print(min1,zhong,max1)




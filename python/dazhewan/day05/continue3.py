# 1. 输入一个整数用begin绑定,
#   再输入一个整数用end绑定
#   打印从begin开始，到end结束内的全部奇数(不包含end)


begin=int(input("请输入第一个数"))
end=int(input("请输入第二个数"))
while begin<end:
    if begin%2 != 0:
        print(begin)
        
    begin+=1

    #  将上述练习改写为 用while语句实现
num1=int(input("请输入第一个数"))
num2=int(input("请输入第二个数"))
for i in (num1,num2+1):
    if i %2 !=0:
        print(i)
    continue
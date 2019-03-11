# 写一个程序，输入一个开始的整数存于begin变量中
# 输入一个结束的整数，存于end变量中
# 打印从begin到end（不包含end）的每个整数，
# 
begin=int(input("请输入一个整数"))
end=int(input("请输入一个整数"))
a=begin-end
c=min(begin,end)
num=0
count=0
while num<abs(a):
    print("%2d"%(c+num),end=' ')
    count+=1
    num+=1 
    if count%5==0:
        print()

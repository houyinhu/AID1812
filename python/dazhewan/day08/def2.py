
#次示例示意用def语句来定义带有参数的函数
#次函数名为mymax，有两个形式参数a，b用于接收实参的传递
#次函数计算两个参数的最大值并打印
def mymax(a,b):
    print('a=',a)
    print('b=',b)
    if  a>b:
        print(a,'大于',b)
    else:
        print(a,'小于等于',b)
x=int(input("请输入第一个数"))
y=int(input("请输入第二个数"))
mymax(x,y) #函数调用



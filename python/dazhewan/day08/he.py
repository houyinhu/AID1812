# 写一个函数myadd，次函数中的参数列表里有两个参数x，y
# 次函数的功能是打印x+y的和
def myadd(x,y):
    print('和是:',x+y)
myadd(100,200)
myadd("abc",'123')

# 写一个函数print_event，传入一个参数n代表终止的整数，打印
# 0-n之间所有的偶数
def print_event(n):
    for x in range(0,n,2):
        print(x)
n=int(input("请输入"))
v=print_event(n)
print(v)





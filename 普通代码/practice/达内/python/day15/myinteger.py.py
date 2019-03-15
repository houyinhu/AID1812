
#此示例示意自己写一个生成器函数，可以生成从0开始的一系列整数
#到n结束（不包含n）
def myinteger(n):
    i = 0
    while i < n:
        yield i
        i+=1
for x in myinteger(4):
    print(x)





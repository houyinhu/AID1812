
#此示例示意生成器函数的定义和使用
def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("myyield函数运行结束")
g = myyield()   #生成器函数调用将返回生成器对象，g绑定一个生成器
# print(g)
it = iter(g)
print(next(it))





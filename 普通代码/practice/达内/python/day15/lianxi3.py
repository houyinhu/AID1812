
#试写一个生成器函数myfilter，要求此函数与系统内建的filter函数功能完全一致

def myfilter(fn,iterable):
    for a in iterable:
        if fn(a):
            yield a

for x in myfilter(lambda x:x%2 == 0 , range(10)):
    print(x)







L=[1,5,8,9,6]

t=iter(L)
it=iter(range(1,10,3))

# for x in L:
#     print(x)
#for 语句实质就是while，迭代器和rty语句的组合

while True:
    try:
        print(next(it))
    except StopIteration:
        print("访问迭代器结束")
        break













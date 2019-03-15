
def input_number():
    l = []
    while True:
        n = int(input("请输入整数"))
        if n < 0:
            break
        l.append(n)
    return l
l=input_number()
print(l)
print("用户输入的最大数是：",max(l))
print("用户输入的最小数是：",min(l))
print("用户输入的全部数的和是：",sum(l))




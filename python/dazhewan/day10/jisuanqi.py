

def myadd(x,y):
    return x+y

def mysub(x,y):
    return x-y

def mymul(x,y):
    return x*y

def get_func(s):
    if s=='+' or s == '加':
        return myadd
    if s=='*' or s == '减':
        return mymul
    if s in ('*','乘'):
        return mysub

def main():
    while   True:
        s=input("请输入计算公式：")
        L=s.split()
        a=int(L[0])
        b=int(L[2])
        fn = get_func(L[1])
        print("结果是：",fn(a,b))

main()









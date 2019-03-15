

# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

s='asdfsadf'

l=len(s)
def f(s,l):
    if l==0:
        return
    print(s[l-1],end='')
    f(s,l-1)
f(s,l)















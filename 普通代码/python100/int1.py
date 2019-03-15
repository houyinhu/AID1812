
n = int(input('请输入'))

a=1
m=9
while a:
    if m%n==0:
        break
    else:
        m=9*10**a+m
    a+=1
print(m,a)

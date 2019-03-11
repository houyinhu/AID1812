#99乘法表


n=1
while n<=9:
    n1=1
    while n1<=n:
        print(n1,'x',n,'=',(n1*n),end=' ')
        n1+=1
    print()
    n+=1

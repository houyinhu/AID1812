# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

target=int(input('输入一个整数：'))
print(target,'= ',end='')
flag=0
while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i,end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target/=i
            break



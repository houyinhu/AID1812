# 1.输入一个整数，打印正方形的宽和高，打印相应的正方形
count=int(input('请输入一个整数'))
for i in range(1,count+1):
    for j in range(1,count+1):
        print(j,end=' ')
    print()
print('-------')
i=1
for i in range(i,count+i):
    for j in range(i,count+i):
        print('%2d'%j,end=' ')

    i+=1
    print()
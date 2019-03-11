
l=[]
while True:
    n1=int(input("请输入正整数"))
    if n1<0:
        if len(l)<2:
            print("输入的太少")
            continue
        break
    if n1 not in l:
        l+=[n1]
l1=sorted(l)
print("这些数的和是",sum(l))
print("这些数的最大数是",max(l))
print("这些数的第二大数是",l1[-2]) #少个括号
for j in range(len(l)):
    if l[j]==min(l):
        print("删除的最小数是",min(l))
        del l[j]
        break  #没有跳出循环，chaochusuoyin
print(l)
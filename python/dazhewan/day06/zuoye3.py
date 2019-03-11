
n1=int(input("请输入一个数"))
l=[1,1]
n2=0#用来储存最后一个数
for x in range(2,n1+1):
    n2=l[-1]+l[-2]
    l+=[n2]
print(l)



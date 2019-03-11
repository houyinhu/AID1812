n=int(input("请输入一个值"))
count=1#分母
sam=0#累加和
sam1=0
while count<=n:
    sam1=1/count
    sam=sam+sam1
    count+=2
print(sam)

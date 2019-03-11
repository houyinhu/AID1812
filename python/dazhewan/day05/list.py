list1=[]    #创建一个列表,准备存放数字
while True:
    #每次输入一个数,如果次数小于0,则退出循环,否则吧
    #这个数放在列表中
    count=int(input("请输入"))

    if count<0:
        break
    # list1.append(count) 
    list1+=[count]
print(list1)
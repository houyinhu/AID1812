n=int(input("请输入一个值"))
count1=1  
sam=0
n1=1
while count1 <= 2*n:
    sam+=(-1)**(n1+1)*1/count1
    n1+=1
    count1+=2
print(sam)



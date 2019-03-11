num1=int(input("请输入第一个值"))
num2=int(input("请输入第一个值"))
sum1=0
min1=min(num1,num2)
cishu=abs(num1-num2)+1
count=0
while count<cishu:
    sum1+=min1
    min1+=1
    count+=1
print(sum1)


    
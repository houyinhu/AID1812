#  求 1~100 之间所有不被 5, 7, 11 整除的数的和
num=0 #累加和
for i in range(1,101):
    if i%5 != 0 and i%7!=0 and i%2!=0 and i%3!=0:
        num+=i
        print(i,end=' ')
print(num)
for a,b in zip(num,str):
 print(b,'is',a)

for i in range(1,21):
    print(i,end=' ')
print()
for j in range(100):
    if j*(j+1)%11==8:
        print(j,end=' ')
print()
m=1
while m<21:
    print(m,end=' ')
    m+=1
print('-----')

num=0
for i in range(1,100,2):
    num+=i
print(num)
print('-------')

k=1
num1=0
while k < 100:
    num1+=k #用来累加
    k+=2    #向后移2
print(num1)

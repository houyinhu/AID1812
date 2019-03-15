# 有四个数字：1、2、3、4，
# 能组成多少个互不相同且无重复数字的三位数？各是多少？

total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k,sep='',end=' ')
                total+=1
    print()
print(total)
'''
import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)
'''
    # 1 1234  1234
    # 2 1234  1234
    # 3 1234  1234
    # 4 1234  1234
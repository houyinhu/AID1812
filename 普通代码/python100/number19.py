# 题目：一个数如果恰好等于它的因子之和，这个数就称为"
# 完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

sum1=0
for i in range(2,1001):
    for j in range(1,i):
        if i%j==0:
            sum1+=j
    if sum1==i:
        print(i)
    sum1=0




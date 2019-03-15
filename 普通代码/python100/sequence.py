# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。
zi=2
mu=1
num1=0
for i in range(1,21):
    num1+=zi/mu
    # mu ,zi= zi,zi+mu
    n=mu
    mu=zi
    zi=n+zi


print((num1))



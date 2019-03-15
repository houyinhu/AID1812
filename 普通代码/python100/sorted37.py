
# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，
# 选择一个最小的与第一个元素交换，下次类推，
# 即用第二个元素与后8个进行比较，并进行交换

n=[]
while True:
    if len(n) > 9:
        break
    try:
        n.append(int(input("请输入数字")))
    except:
        continue

for i in range(len(n)):
    for j in range(i,len(n)):
        if  n[i] > n[j]:
            n[i],n[j]=n[j],n[i]

print(n)













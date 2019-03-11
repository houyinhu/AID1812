# 打印10以内的偶数（要求使用while语句+continue）
# 采用跳过奇数的方式实现

i=0
while i <=10:
    if i%2 != 0 :
        i += 1
        continue
    print(i)
    i+=1
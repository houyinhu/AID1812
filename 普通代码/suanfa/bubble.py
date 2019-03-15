




# while b>0:
#     for x in range(b):
#         if l[x] > l[x+1]:
#             l[x],l[x+1] = l[x+1],l[x]
#     b-=1


# print(l)


def bubble(value):
    #外层循环：对应走访数据的次数
    for i in range(len(value)-1):
        #内层循环：对应每次走访数据时，相邻数据对比次数
        for j in range(len(value)-1-i):
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]
    #走访数据次数
    print("走访次数：",i+1)

if __name__ == '__main__':
    #原始数据value
    value = [1,5,564,564,54,65,465,465,4654,654,65,4]
    bubble(value)
    print(value)






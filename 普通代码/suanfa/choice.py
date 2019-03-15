
# def insert(value):
#     #外层循环：对应遍历所有无序数据，找出插入数据
#     for i in range(1,len(value)):
#         #备份取出数据
#         temp = value[i]
#         #记录取出时的下标值
#         pos = i

#         #内层循环：对应从后向前扫描所有有序数据
#         #1-》从最后一个有序数据开始，即无需数据前一位
#         #2-》扫描到下一位
#         #3-》从后想前扫描
#         for j in range(i-1,-1,-1):
#             if value[j] > temp:
#                 #有序数据后移
#                 value[j+1] = value[j]
#                 #更新数据的插入位置
#                 pos = j
#             #若有序数据小于等于取出数据
#             else:

#                 #更新数据的插入位置
#                 pos = j+1
#                 break
#         #在指定位置插入数据
#         value[pos] = temp



def insert(value):
    #外层循环：对应遍历所有无序数据，找出插入数据
    for i in range(1,len(value)):

        ss = value[i]
        index = i-1

        while index>=0 and value[index]>ss:
            value[index+1] = value[index]
            value[index] = ss
            index -=1

if __name__ == '__main__':
    #原始数据
    value = [15,35,453,453,45,646,5,435,45,854]
    #插入排序
    print("排序前：",value)
    insert(value)
    print("排序后：",value)






import random


#原始数据data
# #待查找数据 key
# def linear(data,key):
#     for i in data:
#         #对比当前数据与待查找数据
#         if i == key:
#             #查找成功，返回下表值
#             return data.index(i)
#     else:
#         #遍历完仍未找到数据
#         return -1

#当前查找范围为的首元素下标值 left 
#当前查找范围的尾元素下标值 right
def binary(value,key,left,right):
    #递归的退出条件
    if left > right:
        #查找结束，未找到
        return -1
    #获取中间元素对应下标值
    middle = (left+right) // 2
    #对比中间元素和查找元素
    if value[middle] == key:
        #查找成功
        return middle
    elif value[middle] >key:
        #若中间元素大于待查找元素值
        #则在左侧继续查找
        #查找范围减半：左侧下标值不变，右侧下标志变为middle上一位
        return binary(value,key,left,middle-1)
    elif value[middle] < key:
        #若中间元素小于待查找元素值
        #则在右侧继续查找
        #查找范围减半：右侧下标值不变，左侧下标值变为middle下一位
        return binary(value,key,middle+1,right)

if __name__ == '__main__':
    #原始数据
    value = []
    for x in range(1,14):
        value.append(x)
    #待 查找的数据
    key = 8
    # random.shuffle(value)
    #获取返回结果并输出
    # res = linear(value,key)
    res = binary(value,key,0,len(value)-1)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功，是第%s张牌"%(res+1))

    





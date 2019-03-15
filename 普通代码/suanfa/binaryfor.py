#二分查找

#循环实现

def binary(value,key):
    #获取当前数据左侧/右侧下标值
    left = 0
    right = len(value) -1
    #若存在合法范围则继续查找
    while left<=right:
        #获取中间值
        middle = (left+right) //2
        #比较查找值与中间值
        if value[middle] == key:
            #查找成功
            return middle
        elif value[middle] > key:
            #若中间值大于查找值，在左侧查找,左侧下标值不变/右侧变种middle前一位
            right = middle - 1
        elif value[middle] < key:
            #若中间值小于查找值，在右侧查找，右侧下标值不变/左侧下标值变为middle后一位
            left = middle + 1
    #遍历完所有数据仍未找到，查找失败
    return -1



    

if __name__ == '__main__':
    #原始数据
    value = []
    for x in range(1,14):
        value.append(x)
    #待 查找的数据
    key = 6

    res = binary(value,key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功，是第%s张牌"%(res+1))

    




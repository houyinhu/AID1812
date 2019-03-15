#快速排序

def quick(value):
    #递归退出条件
    #仅剩一个元素无需继续分组
    if len(value) < 2:
        return value
    #设置关键数据
    A = value[0] 
    #找出所有笔A大的数据
    big = [x for x in value if x >A]
    #找出所有比A小的数据
    small = [x for x in value if x < A]
    #找出所有和A相等的数据
    equal = [x for x in value if x == A]
    #皮接数据排序结果
    return  quick(small) + equal + quick(big)
    
if __name__ == '__main__':
    #原始数据
    value = [15,35,453,453,45,646,5,435,45,854]
    #插入排序
    print("排序前：",value)
    a = quick(value)
    print("排序后：",a)










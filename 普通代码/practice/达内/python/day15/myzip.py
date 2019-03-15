

#此示例用生成器函数来创建一个与zip函数功能一致的函数
def myzip(iter1,iter2):
    it1 = iter(iter1)   #拿到第一个参数迭代器
    it2 = iter(iter2)
    while True:
        try:
            v1 = next(it1)
            v2 = next(it2)
            yield (v1,v2)
        except StopIteration:
            return

numbers = [10086,10000,1001,95588]
names = ['中国移动','中国电信','中国联通']
for t in myzip(numbers,names):
    print("t=",t)







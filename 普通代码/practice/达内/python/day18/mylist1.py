
#重写str函数

#自定义列表
class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    #重写__abs__()函数
    def __abs__(self):
        return Mylist(abs(x) for x in self.data)

    def __str__(self):
        ret = ""
        for x in self.data:
            ret += str(x )  #将元素由数字转换成字符串
            ret +=" "
        return ret

if __name__ == "__main__":
    L = Mylist([-1,2,-3,4,4.124])
    #打印自定义列表中所有元素的绝对值
    L2 = abs(L) #重写了__abs__()函数，支持abs表达式
    print(L2)    #重新了__str__()函数，所以支持print()








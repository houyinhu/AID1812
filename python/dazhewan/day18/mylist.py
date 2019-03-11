
#自定义列表

class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    #重写__abs__()函数
    def __abs__(self):
        return Mylist([abs(x) for x in self.data])

if __name__ == "__main__":
    L = Mylist([-1,2,-3,4,4.124])
    #打印自定义列表中所有元素的绝对值
    # for x in L.data:
    #     print(abs(x))
    # print("---------------------")
    # #取所有元素近似值打印
    # for x in L.data:
    #     print(round(x,2))
    print(abs(L))













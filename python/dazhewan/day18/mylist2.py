
#自定义列表

#重写len函数    round函数 reversed函数

class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    def __len__(self):  #重写__len__函数，返回元素个数
        return len(self.data)

    def __round__(self,n=None):
        return [round(x,n) for x in self.data]

    def __reversed__(self):
        return self.data[::-1]

if __name__ == "__main__":
    L = Mylist([-1,2,-3,4,4.124])
    c = len(L)  #打印返回的长度
    print(c)

    r1 = round(L,2)
    print(r1)   #打印新产生的对象，每个元素都是原对象元素的近似值

    print(reversed(L))











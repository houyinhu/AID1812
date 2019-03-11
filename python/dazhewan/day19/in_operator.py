
#自定义列表

#in / not in 运算符重载
class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    def __contains__(self, item):
        print("__contains__()被调用")
        return item in self.data


if __name__ == "__main__":
    L1 = Mylist([1,-1,15,2,3])
    print(2 in L1)
    print(4 not in L1)






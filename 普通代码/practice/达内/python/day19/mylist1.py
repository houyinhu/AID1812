
#自定义列表

#重写len函数    round函数 reversed函数

class Mylist:
    def __init__(self,load):
        self.load = load

    def __lt__(self, other):#小于
        if self.load < other.load:
            return True
        else:
            return False

    def __gt__(self, other):    #大于
        if self.load > other.load:
            return True
        else:
            return False

    def __eq__(self, other):#等于
        if self.load == other.load:
            return True
        else:
            return False

    def __ne__(self, other):#不等于
        if self.load != other.load:
            return True
        else:
            return False

if __name__ == "__main__":
    L1 = Mylist([1,2,4])
    L2 = Mylist([1,2,3])
    L3 = Mylist([1,2,3,4])

    print(L1 < L2)
    print(L3 > L2)
    print(L1 == L2)
    print(L1 != L2)







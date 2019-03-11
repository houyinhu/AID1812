# 此示例示意 索引/切片 运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __getitem__(self, i):

        return self.data[i]



L1 = MyList([1, -2, 3, -4, 5])
L2 = L1[1::2]
print(L2)
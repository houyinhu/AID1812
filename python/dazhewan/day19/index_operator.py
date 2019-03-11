
#自定义列表

#索引运算操作符
class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    def __getitem__(self, item):#重载取值操作
        return self.data[item]

    def __setitem__(self, key, value):#重载赋值操作
        self.data[key] = value

    def __delitem__(self, key):#重载索引删除操作
        del  self.data[key]

    def __str__(self):
        ret = ""
        for x in self.data:
            ret += str(x )  #将元素由数字转换成字符串
            ret +=" "
        return ret

if __name__ == "__main__":
    L1 = Mylist([1,-1,15,2,3])
    print(L1[2])    #取值
    print(L1)
    L1[3]=333
    print(L1)
    del L1[2]   #删除
    print(L1)






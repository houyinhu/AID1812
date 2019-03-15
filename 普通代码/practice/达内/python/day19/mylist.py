
#自定义列表

#重写len函数    round函数 reversed函数

class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    def __eq__(self, other):#重载==运算符
        len1 = len(self.data)
        len2 = len(other.data)
        if len1 != len2:    #长度不相等无需比较
            return False
        for i in range(0,len1):
            if self.data[i] != other.data[i]:
                return False    #只要出现元素不相等，返回False
        return True

    def __ne__(self, other):
        return not(self == other)


    def __gt__(self, other):#取data属性长度
        print("__gt__()方法被调用")
        len1 = len(self.data)
        len2 = len(other.data)
        min_len = min(len1,len2)
        for x in range(min_len):    #以长度短的作为循环
            if self.data[x] > other.data[x]:
                return True
            if  self.data[x] == other.data[x]:
                continue
            if self.data[x] < other.data[x]:
                return False
        if len1 == len2:
            return False
        if len1 >len2:
            return True
        else:
            return False

    def __str__(self):
        ret = ""
        for x in self.data:
            ret += str(x )  #将元素由数字转换成字符串
            ret +=" "
        return ret

if __name__ == "__main__":
    L1 = Mylist([1,2,3])
    L2 = Mylist([1,2,4])
    print(L1 == L2)
    print(L1 > L2)
    print(L1 < L2)
    print(L1 != L2)









#自定义列表

#一元运算符
class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]

    def __neg__(self):#重载负号运算符
        return Mylist(-x for x in self.data)

    def __str__(self):
        ret = ""
        for x in self.data:
            ret += str(x )  #将元素由数字转换成字符串
            ret +=" "
        return ret

if __name__ == "__main__":
    L1 = Mylist([1,-1,15,2,3])
    print(-L1)   #对对象执行符号运算






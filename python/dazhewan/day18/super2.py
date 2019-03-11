
class A:
    def __init__(self,name):
        self.name = name

    def __str__(self):#重写__str__函数
        return "name = %s"%self.name

class B(A):
    def __init__(self,name,id):
        super().__init__(name)    #调用父类构造方法
        self.id = id        #id属性被创建

    def __str__(self):
        return "name = %s,id = %s"%(self.name,self.id)


b = B("Jerry","0001")
print(b)    #B类中重写__str__方法，所以可以直接打印
str_obj = str(b)    #将b这个对象转换成字符串
print(str_obj)







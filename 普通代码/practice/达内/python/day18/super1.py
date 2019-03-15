
class A:
    def __init__(self,name):
        self.name = name

    def myprint(self):
        print("name = %s"% self.name)

class B(A):
    def __init__(self,name,id):
        super().__init__(name)    #调用父类构造方法
        self.id = id        #id属性被创建

    def myprint(self):
        print("name = %s,id = %s "% (self.name,self.id))

b = B("Jerry","0001")
super(B,b).myprint()  #根据对象b找到父类，并调用父类的print
print(b.id)
print(b.name)

# print(issubclass(B,A))
# print(issubclass(B,object))
# print(issubclass(B,(A,object)))
# print(issubclass(A,B))







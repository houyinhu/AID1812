


# super函数示例
class A():
    def work(self):
        print("A类的work被调用")

class B(A):
    def work(self):
        print("B类的work被调用")
b = B()
super(B,b).work()


class B(A):
    def work(self):
        print("B类的work被调用")
    def super_work(self):
        super().work()
b = B()
b.super_work()


















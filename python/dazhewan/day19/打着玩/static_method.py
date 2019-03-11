# static_method.py

class A:
    @staticmethod
    def myadd(a,b):
        return a+b

print(A.myadd(100,200))
a = A() #创建实例
print(a.myadd(300,400))

print("-----------------------")
def myadd1(a,b):
    return a+b

print(myadd1(100,200))
print(myadd1(300,400))














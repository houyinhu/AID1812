

a=1
def f(a):
    print(a)
    return
f(a=10)
print(a)

创建类
class ClassName(bases):
    'class string'
    class_suite

类下有
属性 attribute 类下定义的变量
方法 method 类下定义的函数  实现了数据的封装
调用时  直接操作    对象内部的数据
无需知道    方法内部的实现细节

命名 动词+对象
第一个参数  self   必须有   
class Bird(object):
    have_feather = True #属性
    def move(self,dx,dy):#方法
        pass
object 
创建示例对象 bird = Bird()   bird 是个对象
属性的引用  bird.have_feather
方法的引用  bird.move(x,y)

__init__(self,..)
特殊方法    类的始化方法/构造函数
用于初始化 创建[实例对象]时回自动调用   强制绑定属性

self（类的实例）
定义类的方法时 永远第一个参数
把各种属性绑定到self
class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
emp1 = Employee('zhang',2000)
通过__init__方法    接受参数



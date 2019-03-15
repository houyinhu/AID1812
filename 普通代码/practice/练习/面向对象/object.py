
# 向把一切看成对象（示例），对象和对象之间建立惯量关系

# class 类名（继承列表）：
#     语句

# 继承列表 该类继承的父类

# class Dog:
#     pass
#
# #创建第一个实例
# dog1 = Dog()
# dog1.kinds="京巴" #添加实例变量
# dog1.color="白色"
# dog1.color="黄色" #改变实例变量的绑定关系
# print(id(dog1))
# print(dog1.kinds)
# #创建第二个实例
# dog2 = Dog()    #绑定一个Dog类型的对象
# dog2.kinds = "藏獒"
# dog2.color = "棕色"
# print(id(dog2))
# print(dog2.color)
# 实例也叫对象，通常是指用类的构造函数创建出来的对象

#实例变量
# 实例.变量名
# del语句可以用来删除实例变量
# del 对象.变量名

# 实例方法
# class 类名（继承列表）：
#     def 实例方法名（self,参数1，参数2...):
#     ''文档字符串''
#     语句块
#实例方法对的第二个器的参数时构造函数调用时传入的参数

# class Dog:
#     def eat(self,food):
#         print("小狗正在吃",food)
#     def sleep(self,hour):
#         print("小狗睡了",hour,'小时！')
# dog1 = Dog()
# dog1.eat('骨头')
# dog1.sleep(1)
#
# Dog.eat(dog1,'狗粮')
# Dog.sleep(dog1,4)


# 初始化方法
# class 类名（继承列表）：
#     def __init__(self[,参数列表])：
#         语句块

#类方法
# class A:
#     v=10
#     @classmethod
#     def set_v(cls,value):
#         cls.v = value
#     @classmethod
#     def get_v(cls):
#         return cls.v
#
# print(A.get_v())
#
# A.set_v(100)
# print(A.get_v())


#静态方法只能凭借该类创建的实例调用
#静态方法不能访问类变量和属性














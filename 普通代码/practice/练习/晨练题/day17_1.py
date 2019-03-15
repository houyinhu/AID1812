
# 练习1：
# 写一个最简单的类(理解类、属性、对象的含义)，要求如下：
# 定义一个类Student，学生信息有姓名、手机号、邮箱
# 在类中定义三个方法，分别获取学生的姓名，手机号及邮箱
# s1 = Student("Bob","13888888888","666666@qq.com")
# 分别打印学生的 姓名、手机号和邮箱

# class Student():
#     def __init__(self,name,phone,emal):
#         self.name = name
#         self.phone = phone
#         self.emal = emal
#
#     def obtain_name(self):
#         print(self.name)
#
#     def obtain_phone(self):
#         print(self.phone)
#
#     def obtain_emal(self):
#         print(self.emal)
#
# s1 = Student("Bob","13888888888","666666@qq.com")
#
# s1.obtain_name()
# s1.obtain_phone()
# s1.obtain_emal()




# 练习2：                             # __slots__属性
class Salary:
    total_money = 500000
    __slots__ = ["name","salary",'month']
    def __init__(self,name,salary,month):
        self.name,self.salary,self.month = name,salary,month
    @classmethod
    def total_salary(cls):
        print("总工资为：",cls.total_money)
a1 = Salary("wang",1000,3)
# (1). 此程序运行会出现1个问题，请改正后做第(2)题
# (2). 改变类变量total_money的值，使print(a1.total_money)的结果为 1000000

a1.__class__.total_money = 100000
# Salary.total_money = 1000000
print(Salary.total_money)
print(a1.__class__)








#staff.py
#员工类，演示__slots__属性示例

class Staff:
    "这是一个员工类"
    "这是类中的第二个不赋值的字符串"
    __slots__ = ['no','name','position']
    def __init__(self,no,name,position):
        self.no  = no   #员工编号
        self.name = name    #员工姓名
        self.position = position #职位
        # self.salary=800 #不允许

    def __str__(self):
        ret = "编号:%s,姓名:%s,职位:%s"%(
            self.no,self.name,self.position
        )
        return ret

if __name__ == '__main__':
    staff = Staff('0001','ja','经理')
    #如果没有__slots__属性，则创建一个新属性
    #执行不会报错，但没有起到给属性赋值的作用
    # staff.position12 = '副总经理'
    print(staff)
    print(staff.__doc__)












#mynumber.py
#此示例示意让重写repr和str方法改变转为字符串的规则

class Mynumber:
    def __init__(self,value):
        '构造函数，初始化MyNumber对象'
        self.data = value

    def __str__(self):
        '''转化为普通人识别的字符串'''
        # print("__str__方法被调用！）
        return '自定义数字类型对象：%d'%self.data

    def __repr__(self):
        '''转换为eval能够识别的字符串'''
        return 'MyNumber(%d)'%self.data

n1 = Mynumber(100)
n2 = Mynumber(200)
print('repr(n1)====>',repr(n1))
print('str(n1)====>',str(n1))








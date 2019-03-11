
#my_number.py
#自定义数字类型
#数值转换函数重写示例
class MyNumber:
    def __init__(self,value):
        self.data = value   #值，字符串类型

    def __int__(self):
        return int(float(self.data))

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)


if  __name__ == "__main__":
    mynumber = MyNumber('123.45')

    print(getattr(mynumber,'data'))
    # print(mynumber.data)

    # setattr(mynumber,'data','456.78')
    mynumber.data = '456.78'
    print(getattr(mynumber,'data'))

    print(hasattr(mynumber,'data')) #True
    print(hasattr(mynumber,'aaa'))  #False

    delattr(mynumber,'data') #删除data属性
    print(hasattr(mynumber,'data')) #False

    # print(int(mynumber)) #将num对象转换成int
    #
    # print(float(mynumber))
    #
    # print(complex(mynumber))














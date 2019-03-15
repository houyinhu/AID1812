
#operation_attribute.py
#属性管理函数：操作对象属性

class MyNumber:
    def __init__(self,value):
        self.data = value   #值，字符串类型

if  __name__ == "__main__":
    mynumber = MyNumber('123.45')

    #getattr:获取对象属性值
    print(getattr(mynumber,'data'))
    # print(mynumber.data)

    #setattr:设置对象属性值
    # setattr(mynumber,'data','456.78')
    mynumber.data = '456.78'
    print(getattr(mynumber,'data'))

    #hasattr:判断有没有某个属性值
    print(hasattr(mynumber,'data')) #True
    print(hasattr(mynumber,'aaa'))  #False

    #delattr:删除对象某个属性值
    delattr(mynumber,'data') #删除data属性
    print(hasattr(mynumber,'data')) #False














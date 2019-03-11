


# (7) 调用 print(hydrogen)，然后修改 Element 的定义，将 dump 方法的名字改为 __str__。
# 再次创建一个 hydrogen 对象并调用 print(hydrogen)，观察输出结果



class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return ("naem:%s symbol:%s number:%s "%(self.name,self.symbol,self.number))


hydrogen = Element('Hydrogen','H',1)


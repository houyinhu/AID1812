
#element2.py
# (8) 修改 Element 使得 name、symbol 和 number 特性都变成私有的。为它们各
# 定义一个 getter属性来返回各自的值。

class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def get_name(self):
        return self.__name
    def get__symbol(self):
        return self.get__symbol
    def get__number(self):
        return self.get__number


hydrogen = Element('Hydrogen','H',1)
print(hydrogen.get_name())

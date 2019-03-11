
#element.py

# (4) 创建一个名为 Element 的类，它包含实例特性 name、symbol 和 number。
# 使用 'Hydrogen'、'H' 和 1 实例化一个对象


class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("naem:%s symbol:%s number:%s "%(self.name,self.symbol,self.number))

element = Element('Hydrogen','H',1)

# 5创建一个字典，包含这些键值对：'name': 'Hydrogen'、'symbol': 'H' 和
# 'number': 1。然后用这个字典实例化 Element 类的对象 hydrogen。

dict1 = {'name':'Hydrogen','symbol':'H','number':1}
element .name=dict1['name']


hydrogen = Element('Hydrogen','H',1)
hydrogen.dump()






#named_tuple.py

#命名元组
from collections import namedtuple
class Bill():
    def __init__(self,description):
        self.description = description

class Tail():
    def __init__(self,length):
        self.length = length

class Duck():
    def __init__(self,bill,tail):
        self.bill = bill
        self.tail = tail

Duck = namedtuple('Duck','bill tail')
duck = Duck('wide orange','long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill':'wide orange','tail':'long'}
duck2 = Duck(**parts)#同：duck2 = Duck(bill = 'wide orange', tail = 'long')
print(duck2)


# 命名元组是不可变的，可以替换其中某些域的值并返回一个新的命名元组：
duck3 = duck2._replace(tail='magnificent',bill='crushing')
print(duck3)

#把 duck 定义为字典：
duck_dict = {'bill':'wide orange','tail':'long'}
print(duck_dict)
#向字典里添加新的域（键值对）：
duck_dict['color'] = 'green'
print(duck_dict)
#但无法对命名元组这么做：
# duck.color = 'green'

# 它无论看起来还是使用起来都和不可变对象非常相似；
# • 与使用对象相比，使用命名元组在时间和空间上效率更高；
# • 可以使用点号（.）对特性进行访问，而不需要使用字典风格的方括号；
# • 可以把它作为字典的键。
#myiterator.py

#此示例示意让自定义的作为可迭代对象能让for语句迭代访问

class MyList:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)"%self.data

    def __iter__(self):
        '''此方法必须返回一个迭代器对象
        此方法创建一个迭代器对象并返回'''
        return MyListIterator(self.data)

class MyListIterator():
    '''此类用来创建迭代器，此类型的迭代器可以迭代访问
    MyList类型的对象'''
    def __init__(self,lst):
        self.data = lst
        self.cur_index = 0  #初始化跌打器的起始位置

    def __next__(self):
        '''此方法用于实现迭代器协议'''
        if self.cur_index >= len(self.data):
            #如果索引越界就发终止迭代通知
            raise StopIteration
        value = self.data[self.cur_index]   #返回的值
        self.cur_index +=1
        return value
my1 = MyList([0,-1,2,-3])
print(my1)

it = iter(my1)
print(next(it))
print(next(it))
print(next(it))


for x in my1:   # 迭代访问自定义类型的对象
    print(x)






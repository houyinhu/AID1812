
#thing2.py

# (2) 创建一个新的类 Thing2，将 'abc' 赋值给类特性 letters，打印 letters
class Thing2():
    letters = 'abc'
print(Thing2.letters)


# (3) 再创建一个新的类，叫作 Thing3。这次将 'xyz' 赋值给实例（对象）特性 letters，并
# 试着打印 letters。看看你是不是必须先创建一个对象才可以进行打印操作？

class Thing3():
    pass
let = Thing3()
let.letters = 'abc'
print(let.letters)

print(Thing3.__dict__)



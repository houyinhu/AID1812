#truck.py
#卡车类，演示运算符的重载

class Truck:
    def __init__(self,load):
        self.load = load    #载重

    def __add__(self, other):
        return Truck(self.load + other)

    # 复合运算符重载，支持obj += 2 表达式
    def __iadd__(self, other):
        return Truck(self.load + other)

    def __str__(self):
        print("__add__()被调用")
        return "load:%d"%self.load

if __name__ == "__main__":
    truck = Truck(20)

    truck+=5    #调用__iadd__()方法 如果没有调用__add__()
    print(truck)












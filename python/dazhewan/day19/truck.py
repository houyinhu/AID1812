#truck.py
#卡车类，演示运算符的重载

class Truck:
    def __init__(self,load):
        self.load = load    #载重

    def __add__(self, value):   #重载+运算符
        return Truck(self.load+value)

    def __mul__(self, other):   #重载乘号运算符
        return Truck(self.load * other)

    #方向+运算符重载，支持3+truck操作
    def __radd__(self, other):
        print("__radd__()被调用")
        return Truck(self.load + other)

    def __str__(self):
        print("__add__()被调用")
        return "load:%d"%self.load

if __name__ == "__main__":
    truck = Truck(20)
    truck2 = truck + 1
    truck3 = truck * 2
    print(truck2)
    print(truck3)

    truck4 = 2 + truck
    print(truck4)











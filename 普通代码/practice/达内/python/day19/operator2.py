#truck.py
#卡车类，演示运算符的重载

class Truck:
    def __init__(self,load):
        self.load = load    #载重

    def __gt__(self, other):#重载>运算符
        if self.load > other.load:
            return True
        else:
            return False
    def __lt__(self, other):#重载小于运算符
        if self.load < other.load:
            return True
        else:
            return False
    def __str__(self):
        print("__add__()被调用")
        return "load:%d"%self.load

if __name__ == "__main__":
    truck = Truck(20)
    truck1 = Truck(25)
    print(truck>truck1) #调用__gt__()
    print(truck<truck1) #调用__lt__()

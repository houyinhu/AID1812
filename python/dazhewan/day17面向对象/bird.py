
#鸟类
class Bird:
    def __init__(self,species):
        self.species = species

    def eat(self):  #吃方法
        print("%s正在吃食物"%self.species)

    def fly(self):  #飞行方法
        print("%s正在飞行"%self.species)

    def reproduction(self):
        print("%s是卵生"%self.species)















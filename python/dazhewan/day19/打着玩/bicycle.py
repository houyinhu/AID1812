# 练习:
#   写一个类Bicycle类 ,有 run方法.调用时显示骑行里程km
#     class Bicycle:
#         def run(self, km):
#             print('自行车骑行了', km, '公里')
#   再写一个类EBicycle(电动自行车类), 在Bicycle类的基础上添加了电池电量 volume 属性, 有两个方法:
#      1. fill_charge(self, vol)  用来充电, vol为电量
#      2. run(self, km) 方法每骑行10km消耗电量1度,同时显示当前电量,当电量耗尽时调用 父类的run方法继续骑行

#     b = EBicycle(5)  # 新买的电动有内有5度电
#     b.run(10)  # 电动骑行了10km还剩 4 度电
#     b.run(100)  #电动骑行了40km,还剩0度电,其余60用脚登骑行
#     b.fill_charge(10)  # 又充了10度电
#     b.run(50)  # 骑行了50公里剩5度


class Bicycle:
    def run(self,km):
        print('自行车骑行了',km,'公里')

#电动自行车类
class Ebicycle(Bicycle):
    def __init__(self,volume):
        self.volumer = volume   #电量

    def fill_charge(self,vol):
         self.volumer += vol
         print("电动车充电%d度,剩余%s度电"%(vol,self.volumer))

    def run(self,km):
        v = km/10 #消耗电量
        if v <= self.volumer:
            self.volumer -= v
            print('电动车骑行了%s米,还剩%s度电'%(km,self.volumer))
        else:
            vo1 = self.volumer * 10
            self.volumer=0
            km1 = km - vo1

            print("电动车骑行了%s,还剩%s度电，其余用脚蹬骑行%s米"%
                     (vo1,self.volumer,km1))

b = Ebicycle(5)
b.run(10)
b.run(100)
b.fill_charge(10)
b.run(50)





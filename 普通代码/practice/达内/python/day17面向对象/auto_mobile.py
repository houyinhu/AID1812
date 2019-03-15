import random

#汽车类
class Auto_mobile():
    #构造方法，主要作用是对属性初始化
    def __init__(self,name,color,output_volumn):
        self.name = name    #名称
        self.color = color  #颜色
        self.output_volumn = output_volumn  #排量
        self.__distance = 0.0   #属性私有化 前面加两个下划线
        self.__consumption = 8    #每百公里耗油量
        # self.oil = 100         #油量

    def __calc_distance(self):#计算行驶里程方法
        self.__distance += random.randint(1,400)

    def get_distance(self):#获得行驶里程
        return  self.__distance  #返回行驶里程属性

    def startup(self):#启动方法
        print("汽车启动")

    def run(self):#行驶方法
        self.__calc_distance()  #调用行驶里程计算方法
        real_fuel_con = self.__distance/100*self.__consumption  #耗油量
        print("汽车行驶了%.2f公里，油耗%.2f升"%(self.__distance,real_fuel_con))

    def stop(self):#停止方法
        print("汽车停止")

    def info(self):#打印汽车信息
        print("名称:%s,颜色:%s,排量:%.2f"%(self.name,self.color,self.output_volumn))

if __name__ == "__main__":
    #实例化：根据类创建对象（根据模型制作具体产品）
    auto_mobile = Auto_mobile("家用汽车",'红色',2.0)
    auto_mobile.startup()   #启动汽车（调用汽车方法）
    auto_mobile.run()   #行驶
    auto_mobile.stop()  #停止
    auto_mobile.info()  #查看汽车对象信息
    #通过调用get_distance()获取行驶里程
    print("行驶里程：%.2f"%auto_mobile.get_distance()) #打印行驶里程
    # print("剩余油量：%.2f"%auto_mobile.oil)






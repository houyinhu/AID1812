from auto_mobile import *
#家用小汽车类，继承示例
class Car(Auto_mobile):
    pass

if __name__ == "__main__":
    mycar = Car("小汽车","蓝色",1.40)
    mycar.startup() #启动
    mycar.run() #行驶
    mycar.stop()    #停止
    mycar.info()    #打印信息








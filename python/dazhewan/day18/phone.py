
import time
#手机类
class Phone:
    def __init__(self,name,sprice,cpu,screen_size):
        self.name = name    #名称
        self.sprice = sprice    #价格
        self.cpu = cpu  #cpu
        self.screen_size = screen_size  #尺寸

    def startup(self):  #开机方法
        print("%s手机，正在开机"%self.name)
        time.sleep(2)
        print("开机成功")

    def shutdown(self): #关机方法
        print("%s手机，正在关机"%self.name)
        time.sleep(2)
        print("关机成功")

    def call(self,phone_no):     #打电话方法
        print("正在拨号")
        time.sleep(1)
        print("正在和%s通话"%phone_no)

    def send_msg(self,phone_no,msg): #发短信方法
        print("正在向%s发短息"%phone_no)
        time.sleep(2)
        print("[%s]发送成功"%msg)

    def __del__(self):#析构函数
        print("__del__方法被调用")

def fun():
    phone = Phone("小米",5400,"双核2G",5.5)
    print("fun()函数退出")

if __name__ == "__main__":
    phone = Phone("华为",5400,"双核2G",5.5)
    # phone.startup() #启动
    # phone.call('阿虎')    #打电话
    # phone.send_msg('阿虎','你好帅')  #发短信
    # phone.shutdown()    #关机
    fun()
    # del phone   #会执行对象的析构函数
    # print("程序退出")







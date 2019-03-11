


#此示例示意函数装饰器的使用
#以银行存取款业务为例。来为存取款业务添加新的功能
#1.添加了权限验证
#2.添加了短消息提醒


#以下是小钱写的装饰器
def privileged_check(fn):
    def fx(n,x):
        print("正在检查权限..")
        fn(n,x)
    return fx

def send_message(fn):
    def fy(n,x):
        fn(n,x)
        print("正在发短消息给", n   )
    return fy

#----以下是魏老师写的程序
@send_message
@privileged_check
def savemoney(name,x):
    print(name,'存钱',x,'元')

@privileged_check
def withdraw(name,x):
    print(name,'取钱',x,'元')

#----以下是调用者小张写的程序
savemoney('小王',200)
savemoney('小赵',400)
withdraw('小李',500)














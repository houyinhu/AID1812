#account.py
import datetime
datetime.timedelta

dict_status = {
    0:"正常",1:"冻结",2:"挂失",3:"销户"
}
dict_type = {0:"借记账户",1:"贷记账户"}


#作业一
class Account:
    def __init__(self,acct_no,acct_name,reg_date,acct_type,acct_statue,balance):
        self.acct_no = acct_no  #账号
        self.acct_name = acct_name  #户名
        self.acct_type = acct_type  #开户日期
        self.reg_date = reg_date    #账户类型
        self.acct_statue = acct_statue #状态
        self.balance = balance  #余额

    def diposite(self,money):     #存款方法
        if self.acct_statue == 0:
            self.balance += money
            print("存款成功，存款%.2f，余额为：%.2f"%(money,self.balance))
        else:
            print("账户冻结，你不能操作")

    def draw(self,money): #取款方法
        if self.acct_statue == 0:    #正常
            if self.balance < money:    #余额不足
                print("账户余额不足，")
            else:   #余额充足
                print("取款前余额：%.2f"%self.balance)
                self.balance -= money   #修改余额
                print("取款后余额：%.2f"%self.balance)
        else:
            print("账户冻结，你不能操作")

    def freeze(self):   #冻结方法
        self.acct_statue = '冻结'
        print("状态已冻结")

    def unfreeze(self): #解冻方法
        self.acct_statue = '正常'
        print("账户已解冻")

    def report_loss(self):  #挂失方法
        self.freeze()

    def relieve_loss(self): #解除挂失方法
        self.unfreeze()

    def modify_acct_info(self): #查看账户信息方法
        print("户名:%s,账号:%s,开户日期:%s,账户类型:%s,状态:%s,余额:%s"%
              (self.acct_no,self.acct_name,self.reg_date,type,\
               self.acct_statue,self.balance))

    def __str__(self):#重写__str__()
        #将状态转换为对应的字符串
        status = dict_status[self.acct_statue]

        #将类型转换为对应的字符串
        type = dict_type[self.acct_type]
        ret = "户名:%s,账号:%s,开户日期:%s,账户类型:%s,状态:%s,余额:%s" %\
              (self.acct_no, self.acct_name, self.reg_date, type, \
               self.acct_statue, self.balance)
        return ret
if __name__ == '__main__':
    account = Account('阿虎','4102241998',"2019年01月24",0,0,500,)
    account.diposite(500)

    account.draw(500)

    print(account)






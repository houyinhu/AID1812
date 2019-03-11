from customer import *
from staff import *
#chain_store.py
#连锁店类，类属性/类方法示例

class ChainStore:
    #类属性
    store_num = 0#连锁店门店数量
    total_income = 0 #所有门店总营业额
    store_list = [] #所有门店对象列表
    cust_list = []  # 所有会员列表

    def __init__(self,store_no,store_name,
                 address,manager,):
        print('门店开张,')
        self.store_no = store_no    #编号
        self.store_name = store_name    #名称
        self.address = address  #地址
        self.manager = manager  #经理
        self.myincome = 0   #本店营业额度
        ChainStore.store_num += 1   #门店数量，总数量加1
        ChainStore.store_list.append(self)  #添加当前对象到所有门店列表
        self.staff_list = []    #连锁店包含一组员工，组合关系


    def add_staff(self,staff):  #添加员工
        self.store_list.append(staff)

    def remove_staff(self,no):  #删除员工
        for staff in self.store_list:
           if not staff.no == no:
               self.store_list.remove(staff)

    def print_all_staff(self):  #打印所有员工信息
        for staff in self.store_list:
            print(staff)

    def do_business(self,income):  #营业方法
        print('正在营业')
        self.myincome += income #营业额累加
        ChainStore.total_income += income   #将本店的营业额度累加到总营业额

    def __str__(self):#重写__str__()
        ret = '编号:%s,名称:%s,地址:%s,店长:%s,总营业额:%.2f'%(
            self.store_no,self.store_name,
            self.address,self.address,self.myincome
        )
        return ret

    # def __del__(self):#析构函数
    #     print("%s门店关闭"%self.store_name)
    #     ChainStore.store_num -= 1   #减少一家门店

    @classmethod
    def print_total(cls):   #类方法，打印类的属性
        print('门店数量：%d,营业总额度:%.2f'%
              (cls.store_num,cls.total_income))
        for store in cls.store_list:    #遍历门店列表
            print(store)

    @staticmethod
    def print_regulation():#静态方法，打印管理条例
        regulation = '''
        --------连锁店管理条例--------
        第一条：考勤
        第二条：不迟到，
        第三天：请假
        ...
        '''
        print(regulation)

    def cust_reg(self,cust):    #会员注册
        ChainStore.cust_list.append(cust)

    def print_cust_info(self):  #打印会员
        print('员工有：')
        for cust in ChainStore.cust_list:
            print(cust)

if __name__ == "__main__":
    #第一家分店
    store1 = ChainStore('1','东京旗舰店','东京','阿虎')
    store1.do_business(20000)   #营业
    ChainStore.print_total()#调用类方法
    # store1.print_total()

    # store1.cust_reg(Customer('1', '八戒', '13456456456'))
    # store1.cust_reg(Customer('2', '悟空', '13456456456'))
    # store1.print_cust_info()

    #调用静态方法
    # ChainStore.print_regulation()   #类调用
    # store1.print_regulation()   #对象调用

    # print("门店数量:%s,总营业额度:%s"%(ChainStore.store_num,ChainStore.total_income))
    # print()
    #第二家分店
    store2 = ChainStore('2','中关村旗舰店','中关村','阿亮')
    store2.do_business(25000)   #营业
    print("门店数量:%s,总营业额度:%s" % (ChainStore.store_num, ChainStore.total_income))

    del  store2 #销毁store2对象







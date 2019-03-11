
from staff import *
from customer import *
#chain_store.py
#连锁店类，类属性/类方法示例

class ChainStore:
    #类属性
    store_num = 0#连锁店门店数量
    total_income = 0 #所有门店总营业额
    store_list = [] #所有门店对象列表

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


if __name__ == "__main__":
    store1 = ChainStore('1','东京旗舰店','东京','阿虎')
    store1.do_business(20000)   #营业
    store1.add_staff(Staff('0001','j','店长'))
    store1.add_staff(Staff('0002','a','员工'))
    store1.add_staff(Staff('0003','s','员工'))
    store1.print_all_staff()

    store1.cust_reg(Customer('1','八戒','13456456456'))
    store1.cust_reg(Customer('2','悟空','13456456456'))









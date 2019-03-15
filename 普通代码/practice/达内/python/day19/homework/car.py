#car.py

d = {
    "car_id":4001,
    'name':'宝马',
    'if_lend':'否',
    'price':100,
    'start_date':2018,
    'end_date':2019
}

if_lend = {0:'否',1:'出'}

#汽车类
class Car:
    def __init__(self,car_id,name,if_lend,price,start_date,end_date):
        self.car_id = car_id    #车辆id号
        self.name =name         #车辆名称
        self.if_lend = if_lend  #是否出租
        self.price = price      #每天单价
        self.start_date = start_date    #起租日期
        self.end_date = end_date        #租赁终止日期



    def __str__(self):
        return "%s %s %s %s %s %s" % (self.car_id, self.name, self.if_lend, self.price, self.start_date, self.end_date)


#客户类
class Customer():
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id  #客户编号
        self.cust_name = cust_name  #客户姓名
        self.tel_no = tel_no    #客户电话

    def __str__(self):
        return "%s %s %s"%(self.cust_id,self.cust_name,self.tel_no)

#租车店类
class CarStore(Customer,Car):
    def __init__(self,cars,customers):
        self.cars = cars    #所有车辆列表
        self.customers = customers      #所有客户列表

    def __load_cars(self):#加载所有车辆信息
        L = []  #用来存储信息
        try:
            f1 = open(self.cars,encoding='utf-8')
            try:
                while True:
                    lin1 = f1.readline()    #每次取一行信息
                    if not lin1:    #到达文件尾
                        break
                    lst =lin1.strip()
                    s = lst.split(',')
                    name= s[0]  #车辆名称
                    type = s[1] #车辆类型
                    number = s[2]   #车辆数量
                    dict = {'name':name,'type':type,'number':number}
                    L.append(dict)
                print("加载车辆信息成功")
            except:
                f1.close()
        except OSError:
            print("加载车辆信息失败")
        finally:
            f1.close()

    def __load_customers(self): #加载所有客户信息
        L = []  # 用来存储信息
        try:
            f1 = open(self.customers, 'w', encoding='utf-8')
            try:
                while True:
                    lin1 = f1.readline()  # 每次取一行信息
                    if not lin1:  # 到达文件尾
                        break
                    lst = lin1.strip()
                    s = lst.split(',')
                    id = s[0]   #客户编号
                    name = s[1] #客户姓名
                    no = s[2]   #客户电话
                    dict = {'id':id,'name': name,'phone':no}
                    L.append(dict)
                print("加载客户信息成功")
            except:
                f1.close()
        except OSError:
            print("加载客户信息失败")
        finally:
            f1.close()

    def print_cars_info(self):  #打印所有车辆信息
        print("+++++++++++++++++++++++++++++++++++++++++++")
        print("|   车辆id  |   车辆名称  |     是否出租   |")
        for x in self.cars:
            id = x['id']
            name = x['name']
            if_lend = x['if_lend']
            print("|%s|%s|%s|"%(id.center(15),
                                name.center(10),
                                if_lend.center(10)))
        print("----------------------------------------------------")

    def find_car(self): #查找车辆
        n1 = input("请输入车辆id")
        for x in L:
            if x['id'] == n1:
                print(x)
        else:
            print("找不到车辆")

    def add_car(self):  #添加车辆
        while True:
            c1 = []
            car_id =input("请输入id号,或者按回车结束")
            if car_id == '':
                break
            car_name = input("请输入车辆名称,或者按回车结束")
            if car_name == '':
                break
            car_price = input("请输入价格,或者按回车结束")
            if car_price == '':
                break
            is_lend = input("是否出租")
            start_date = input('起租日期')
            end_date = input("租赁终止日期")
            d = {}
            d['id']=car_id
            d['name'] = car_name
            d['price'] = car_price
            d['is_lend'] = is_lend
            d['start_date'] = start_date
            d['end_date'] = end_date
            self.cars.append(d)

    def del_car(self):  #删除汽车
        n1 = "请输入你要删除的车辆id"
        for x in self.cars:
            if n1 == x['id']:
                self.cars.reverse(x)
        else:
            print("找不到车辆id")

    def lend(self): #租车
        while True:
            n1 = input("请选择车型：1（轿车）， 2（客车）")
            n2 = input("1,大众\n"
                       "2,宝马\n"
                       "3,比亚迪\n"
                       "请选择轿车品牌")
            n3 = int(input("请输入租赁天数"))
            print("租车成功")
            n4 = input("请选择你的操作，\n"
                       "按q结束租车，按y继续租车")
            if n4 == 'q':
                break
            if n4 == 'y':
                continue

    def back(self): #还车
        while True:
            print("请输入你要换的车信息")
            n1 = input("请选择车型：1（轿车）， 2（客车）")
            n2 = input("1,大众\n"
                       "2,宝马\n"
                       "3,比亚迪\n"
                       "请选择轿车品牌")
            n4 = input("请选择你的操作，\n"
                       "按q结束还车，按y继续换车")
            if n4 == 'q':
                break
            if n4 == 'y':
                continue














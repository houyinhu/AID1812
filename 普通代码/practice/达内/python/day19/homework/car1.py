#car.py
def __load_cars():#加载所有车辆信息
    try:
        f1 = open('vehicle_information.txt',encoding='utf-8')
        try:
            while True:
                lin1 = f1.readline()    #每次取一行信息
                if not lin1:    #到达文件尾
                    break
                lst =lin1.strip()
                s = lst.split(',')
                car_id = s[0]
                name= s[1]
                is_lend = s[2]
                price = s[3]
                time1 = s[4]
                time2 = s[5]
                dict = {'car_id':car_id,'name':name,
                        'is_lend':is_lend,'price':price,
                        'start_date':time1,'end_date':time2}
                cars.append(dict)
            print("加载车辆信息成功")
        except:
            f1.close()
    except OSError:
        print("加载车辆信息失败")
    finally:
        f1.close()

def __load_customers(): #加载所有客户信息
    try:
        f1 = open('customer_information.txt', encoding='utf-8')
        try:
            while True:
                lin1 = f1.readline()  # 每次取一行信息
                if not lin1:  # 到达文件尾
                    break
                lst = lin1.strip()
                s = lst.split(',')
                id = str(s[0])  # 车辆名称
                name = str(s[1])  # 车辆类型
                phone = str(s[2])  # 车辆数量
                dict = {'name': id, 'type': name, 'number': phone}
                ustomers.append(dict)
            print("加载客户信息成功")
        except:
            f1.close()
    except OSError:
        print("加载客户信息失败")
    finally:
        f1.close()

def print_cars_info():  #打印所有车辆信息
    print("|-------------------------------------------|")
    print("|     车辆id     |   车辆名称  |  是否出租   |")
    for x in cars:
        id = x['car_id']
        name = x['name']
        if_lend = x['is_lend']
        print("|%s|%s|%s|"%(id.center(15),
                            name.center(10),
                            if_lend.center(10)))
    print("|-------------------------------------------|")

def find_car(): #查找车辆
    n1 = input("请输入车辆id")
    for x in cars:
        if x['car_id'] == n1:
            print("id:%s,名字:%s,是否出租:%s,单价%s,起租时间:%s,终止时间%s"%(
                x['car_id'],x['name'],
                  x['is_lend'],x['price'],
                  x['start_date'],x['end_date'],))
            break
    else:
        print("找不到车辆")

def add_car():  #添加车辆
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
        d['car_id']=car_id
        d['name'] = car_name
        d['price'] = car_price
        d['is_lend'] = is_lend
        d['start_date'] = start_date
        d['end_date'] = end_date
        cars.append(d)

def del_car():  #删除汽车
    n1 = input("请输入你要删除的车辆id")
    for x in cars:
        if n1 == x['car_id']:
            cars.remove(x)
            break
    else:
        print("找不到车辆id")

def lend(): #租车
    while True:
        n1 = input("请选择车辆id")
        if n1 =='':
            break
        n3 = int(input("请输入租赁天数"))
        if n3 =='':
            break
        for x in cars:
            if x['car_id'] == n1:
                if x['is_lend'] == "否":
                    x['is_lend'] = '是'
                    print("租车成功")
                    break
                else:
                    print("此车以被租用")
        else:
            print("找不到此车")
        n4 = input("请选择你的操作，\n"
                   "按q结束租车，按y继续租车")
        if n4 == 'q':
            break
        if n4 == 'y':
            continue

def back(): #还车
    while True:
        print("请输入你要还的车信息")
        n1 = input("请输入你的车辆id")
        n2 = input("请输入车辆名字")
        for x in cars:
            if x['car_id'] ==n1:
                if x['is_lend'] =='是':
                    x['is_lend'] = '否'
                    print('还车成功')
                    break
                else:
                    print("此车没有租出")


        n4 = input("请选择你的操作，\n"
                   "按q结束还车，按y继续换车")
        if n4 == 'q':
            break
        if n4 == 'y':
            continue

def save_car():    #保存汽车信息
    try:
        f2 = open("vehicle_information.txt",'w',encoding='utf-8')
        for x in cars:
            f2.write(x['car_id'])
            f2.write(',')
            f2.write(x['name'])
            f2.write(',')
            f2.write(x['is_lend'])
            f2.write(',')
            f2.write(x['price'])
            f2.write(',')
            f2.write(x['start_date'],)
            f2.write(',')
            f2.write(x['end_date'])
            f2.write('\n')
        print("保存汽车信息成功")
    except OSError:
        print("打开文件失败")
    finally:
        f2.close()



cars = []  # 所有车辆列表
ustomers = []  # 所有客户列表
def main():
    while True:
        print("--------------------------------")
        print("1)加载所有车辆信息")
        print("2）加载所有客户信息")
        print("3）打印所有车辆信息")
        print("4）查找车辆")
        print("5）添加车辆")
        print("6）删除汽车")
        print("7）租车")
        print("8）换车")
        print("9）保存汽车信息")
        print("0）退出操作")
        n1 = input("请输入你的操作")
        if n1 == '1':
            __load_cars()
        if n1 == '2':
            __load_customers()
        if n1 == '3':
            print_cars_info()
        if n1 == '4':
            find_car()
        if  n1 == '5':
            add_car()
        if  n1 == '6':
            del_car()
        if n1 == '7':
            lend()
        if n1 == '8':
            back()
        if n1 == '9':
            save_car()
        if n1 == '0':
            break

if __name__ == "__main__":
    main()













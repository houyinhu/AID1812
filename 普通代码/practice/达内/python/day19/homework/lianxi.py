

cars = []    #所有车辆列表
ustomers = []      #所有客户列表
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



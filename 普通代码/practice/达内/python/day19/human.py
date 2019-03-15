#
# 练习:
#  自己写一个'人'类: Human
#   class Human:
#       def set_info(self, name, age, address='未知'):
#           '''此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性'''
#           ...  # << 此处自己实现
#       def show_info(self):
#           '''显示此人的全部信息'''
#           ... # 此处自己实现

class Human:
    def set_info(self,name,age,address='未知'):
        '''此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性'''
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        '''显示此人的全部信息'''
        print("姓名：%s 年龄：%s 家庭住址：%s"%
              (self.name,self.age,self.address))

human = Human()
# human.set_info('小张',20,'北京朝阳区')
# human2 = Human()
# human2.set_info('小李',18)
# human.show_info()
# human2.show_info()

# human = Human()
# human.set_info('小张', 20, '北京市朝阳区')
Human.set_info(human,'小张',20,'北京朝阳区')
human.show_info()


















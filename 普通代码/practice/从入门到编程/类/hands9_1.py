
class Restaurant():
    def __init__(self,restaurant,cuisine):
        self.restaurant_name = restaurant
        self.cuisine_type = cuisine
        self.number_served = 2

    def describe_restaurant(self):
        print("restaurant:",self.restaurant_name)
        print("cuisine:",self.cuisine_type)

    def open_restaurant(self):
        print("餐馆正在营业",end='')
        print(" 有%s个人就餐" % self.number_served)

    def set_number_server(self,number):
    #能够设置就餐人数。
        print(number)
        self.number_served = number

    def increment_number_serbed(self,increase):
        self.number_served += increase

# restaurant=Restaurant('田家小院','火辣')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# restaurant2=Restaurant('阿虎餐厅','温情')
# restaurant2.describe_restaurant()
#
# restaurant3=Restaurant('华梅','高档')
# restaurant3.describe_restaurant()

#练习9.4
# restaurant = Restaurant(1,2)
# restaurant.set_number_server(10)
# restaurant.open_restaurant()
# restaurant.increment_number_serbed(10)
# restaurant.open_restaurant()


#动手 9.3
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def descrube_user(self):
        print("hello ",self.first_name,)

    def greet_user(self):
        print("hello ",self.first_name,"今天你吃饭了吗")

    def increment_login_attempts(self):
    #将属性login_attempts 的值加 1
        self.login_attempts += 1

    def reset_login_attempts(self):
    #将属性login_attempts 的值重置为 0。
        self.login_attempts = 0




# user=User('侯','银虎')
# user.descrube_user()
# user.greet_user()
#
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.reset_login_attempts()
# print(user.login_attempts)

#9_7
class Admin(User):
    def __init__(self,first_name,last_name,prvileges=''):
        super().__init__(first_name,last_name)
        # self.priv = priv
        self.prvileges = Privileges()

    # 9_7
    def show_privileges(self,priv):
        print("管理员的权限",priv)
#
# #9_8
class Privileges():
    def __init__(self,privileges_size='大'):
        self.privileges_size = privileges_size

    def show_privileges(self):
        print("  "+self.privileges_size)
#
#
privilegeslist=['can add post','can delete post','cam ban user']
admin=Admin(privilegeslist,'123')
admin.show_privileges('321')
admin.prvileges.show_privileges()



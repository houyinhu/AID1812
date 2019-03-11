
class Student():
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def Information(self):
        print("学生{},手机号{},邮箱{}".format(self.name,self.phone,self.email))

s1 = Student("Bob",'13888888888','52352＠qq.com')

s1.Information()













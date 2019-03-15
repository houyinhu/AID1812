#myinteger.py

#此示例示意abs函数的重写

class MyInteger:
    def __init__(self,v):
        self.data = v

    def __repr__(self):
        return 'MyInterger(%d)'%self.data

    def __abs__(self):
        v = abs(self.data)
        return MyInteger(v)#用v创建另一个MyInterger对象
    def __len__(self):
        return 10000

myi = MyInteger(1)
print(myi)

I1 = MyInteger(-10)
print('I1 = ',I1)

I2 = abs(I1)
print("I2=",I2)


print('len(I2)=', len(I2))  # 10000
#









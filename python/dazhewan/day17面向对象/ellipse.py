
#面向过程、面向对象编程比较
#计算椭圆周长、面积
a = 2.0 #短半径
b = 3.0 #长半径

len = 2*3.14*a + 4*(b-a)          #2*PI*短半径 + 4(长半径-短半径)
print("a=%f,b=%f,len=%f"%(a,b,len))

area = 3.14 * a * b
print("a={},b={},len={}".format(a,b,area))


#面向对象方式
class Ellipse:  #定义椭圆类
    # #类中的函数称之为方法
    def __init__(self,a,b,):
        self.a = a  #属性：短半径
        self.b = b  #属性：长半径
    def calc_len(self):#计算周长
        return 2*3.14 * self.a + 4 * (self.b-self.a)
    def cale_area(self):    #计算面积
        return 3.14 * self.a * self.b

e = Ellipse(2.0,3.0)    #实例化
len = e.calc_len()  #获得椭圆周长
area = e.cale_area()    #获得椭圆面积
print("a={},b={},len={},area={}".format(e.a,e.b,len,area))


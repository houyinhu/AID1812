
def make_shirt(t='x',z='毛'):
    print("I love Python")
    print(t,'是小号',z,'是一个好货')
make_shirt('xl','羊绒')   #位置参数
make_shirt(z='羊绒',t='xl')   #关键字参数

#默认参数
def make_shirt(t='x',z='I love Python'):
    print('是%s号'%t,z)

make_shirt()
make_shirt(t='xl')

def describe_city(city='Reykjavik',country='Iceland'):
    print("%s is in $s"%(city,country))
describe_city()
describe_city('beijing','china')
describe_city(city='yingguo')






def get_age():
    information=int(input("请输入1~140之间的整数"))
    if information <1 or information>140:
        raise ValueError("年龄超出范围")
    return information

try:
    age = get_age()
    print("用户输入的年龄是：",age)
except ValueError as err:
    print("用户输入的不是1~140的整数，获取年龄失败",err)














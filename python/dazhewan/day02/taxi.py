mileage=int(input("请输入公里数"))
if 0<mileage<=3:
    money=13
elif 3<mileage<=15:
    money=13+2.3*(mileage-3)
elif mileage>15:
    money=13+2.3*(15-3)+3.45*(mileage-15)
else:
    print("输入错误")
print(money)

#   3. BMI指数(Body Mass Index) 以称身体质量指数
#      BMI值计算公式:
#         BMI = 体重(公斤) / 身高的平方(米)
#      例如:
#        一个人69公斤，身高是173公分
#        BMI = 69 / 1.73**2 = 23.05
#     标准表:
#       BMI < 18.5   体重过轻
#       18.5 <= BMI < 24 体重正常
#       BMI > 24  体重过重
height=float(input("请输入身高（小数）"))
weight=float(input("请输入体重(公斤)"))
bmi=weight/height**2
if 0<bmi<18.5:
    print("bmi=",bmi,"体重过轻")
elif 18.5<=bmi<24:
    print("bmi=",bmi,"体重正常")
elif bmi>24:
    print("bmi=",bmi,"体重过重")

n=int(input("请输入1-4:"))
seasons={
    1:'春季有1,2,3,月',
    2:'夏季有4,5,6月',
    3:'秋季有7,8,9月',
    4:'冬季有10,11,12月'}
if n in seasons:
    print(seasons[n])
else:
    print("输入错误")
# 方法二
seasons={} 
    seasons[1]='春季有1,2,3,月'
    seasons[2]='夏季有4,5,6月'
    seasons[3]='秋季有7,8,9月'
    seasons[4]='冬季有10,11,12月'}





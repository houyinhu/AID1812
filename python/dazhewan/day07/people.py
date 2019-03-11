
l=[]
while True:
    d={}
    fist_name=input("请输入你的姓")
    last_name=input("请输入你的名")
    age=input("请输入你的年龄")
    city=input("请输入你的城市")
    if fist_name=='':
        break
    d['fist_name']=fist_name
    d['last_name']=last_name
    d['age']=age
    d['city']=city
    l+=[d]
for x in range(0,len(l)):
    print(l[x]['fist_name']+\
    l[x]['last_name']+\
    l[x]['age']+\
    l[x]['city'])

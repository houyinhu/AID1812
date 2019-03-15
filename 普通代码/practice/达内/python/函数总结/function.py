
#函数参数

# def student(name,age,**kw):
#     if 'school' in kw:
#         #处理school事物
#         pass
#     if 'address' in kw:
#         #处理address事物
#         pass
#     for x in  kw.values() :
#         print(x)
#     print('name:',name,'age:',age,'other:',kw)
#
# student("zhang",24,school="清华",address='北京海淀')

# student('zhang',24,yy='yy',zz='zz')

# def student(name,age,*,school,address):
#     print('name:',name,'aeg:',age,'school:',school,'address',address)
#
# student("zhang",24,address='北京海淀',school="清华")
# student("zhang",24,"清华","北京海淀")
# 命名关键字参数和位置参数不同  命名关键字参数也叫默认参数


def student(name,age,*,school=[11,5],address):
    print('name:',name,'age:',age,'school',school,'address:',address)
# d={'school':"清华",'address':'北京海淀'}
# student("zhang",24,**d)
# student("zhang",24,address='北京海淀','school':"清华",'address':'北京海淀')
# student("zhang",24,address='北京海淀')
# 默认参数一定要用不可变对象
student("zhang",24,address='北京海淀')



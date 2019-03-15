

s='1+2*3'
# r=eval(s)
# print(r)


# x=100
# y=200
# s='x+y+1'
# r=eval(s)
# print(r)
#
# #先创建一个局部作用域的字典
# local_scope = {'x':1,'y':2}
# a=eval(s,None,local_scope)
# print('a=',a)
#
#创建一个全局作用域的字典
globals_scope = {'x':10,'y':20}
b = eval(s,globals_scope)
print('b=',b)

# c=eval(s,{'x':10,'y':20},{'x=',1})
# print('c=',c)








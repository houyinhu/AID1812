
j={'曹操','刘备','孙权'}
js={'曹操','孙权','张飞','关羽'}
jjs=j &js
jnjs=j-js
jsnj=js-j
print("即是经理也是技术员的有谁：",jjs)
print("是经理，但不是技术人员的有谁",jnjs)
print("是技术人员，但不是经理的有谁",jsnj)
if  '张飞'in j:
    print("张飞是经理")
else:
    print("张飞不是经理")
z1=j^js
print("身兼一职的是：",z1)
people=j | js
print("共有%s人"%len(people))



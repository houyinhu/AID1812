
#1，nonlocal语句只能在嵌套函数内部进行使用
#2，对nonlocal变量进行赋值将对外部嵌套函数作用域内的变量进行操作
v=100
def f1():
    v=200
    print("f1.v=",v)
    #此外嵌入另一个函数
    def f2():
        nonlocal v
        v=300
        print("f2.v=",v)
    f2()
    print("f1执行后f1.v=",v)

f1()
print(v)


#当有两层或两层以上函数嵌套时，访问nonlocal变量只对最近一层变量进行操作
v=100
def f1():
    v=200
    print("f1.v=",v)
    #此外嵌入另一个函数
    def f2():
        # nonlocal v
        v=300
        #再嵌入另一个函数
        def f3():
            nonlocal v
            v=400
        f3()
        print("f2.v=",v)
    f2()
    print("f1执行后f1.v=",v)

f1()
print(v)













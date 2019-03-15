#变量范围

# def fun1():
#     x=100
#     def fun2():
#         x=200
#     print(x)
#     fun2()
#     print(x)
# fun1()
# print('----------------')
# b=50
# def fun1():
#     global b
#     b += 10
#     x=100
#     def fun2():
#         print("b=",b)
#         nonlocal x
#         x=200
#     print(x)
#     fun2()
#     print(x)
# fun1()


x=100
def func():
    x=1000
    def fun2():
        global x
        x = 2000
    fun2()
    print(x)
print(x)
func()
print(x)
print("-----------")
x=100
def func():
    x=1000
    def fun2():
        nonlocal x
        x = 2000
    print(x)
    fun2()
    print(x)
print(x)
func()
print(x)

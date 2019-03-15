

#此示例示意闭包的应用

#写一个求x的平方的函数

n=1
age=10
while n<10:
    if  n==3 or n==5:
        print(n,age)
    n+=1
    age+=2

def age1(n):
    if n ==1:
        return 10
    else:
        return age1(n-1)





# def make_power(y):
#     def fn(x):
#         return x**y
#     return fn
# pow2 = make_power(2)
# print('5的平方是：',pow2(5))
# print('6的平房是：',pow2(6))
# pow3=make_power(3)
# print('7的平方是：',pow3(7))
# pow150=make_power(150)
# print(pow150(2))







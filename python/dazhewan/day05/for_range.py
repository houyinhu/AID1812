#注意事项1
i=6
for x in range(1,i): #range函数执行了一次
    print('x=',x,'i=',i)
    i -= 1
#注意事项2  变量可能不被创建的问题
for x in range(4,0):
    print(x)
else:
    print("循环结束后的x=",x)   #出错
    print(x)        #出错
for x in 'ABC':
    for y in '123':
        print(x+y) 


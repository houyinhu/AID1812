

#此示例示意Python的作用域
v=100
def fun1():
    #v=200
    print('fun1,v=',v)
    def fun2():
       # v=300
        print('fun2.v=',v)
    fun2()
    print(v)
fun1()
print("全局的v=",v)

















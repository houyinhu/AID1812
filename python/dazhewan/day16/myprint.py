
import sys

def myprint(*args,sep=' ',end='\n',file=sys.stdout,flush=False):

    flag = False    #当第一次循环后，将此变量置为True
    for  x in args:
        if flag:    #判断是否是第二次或之后打印
            file.write(sep)     #如果是第二次打印则执行此语句
        file.write(str(x))      #将所有数据转为字符串
        flag = True

    #打印最终的end
    file.write(end)

myprint("hello world")
myprint(1,2,3,4)
myprint(5,6,7,8,sep='#')
myprint(5,6,7,8,sep=',',end=' ')










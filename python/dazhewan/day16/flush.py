
#此示例示意文件缓冲的作用及清除方法

fw = open("myflush.txt",'w')

fw.write("hello")   #此处执行的write操作没有真正写在磁盘上
fw.flush()  #清空缓冲区
while True: #进入死循环
    pass

fw.close()




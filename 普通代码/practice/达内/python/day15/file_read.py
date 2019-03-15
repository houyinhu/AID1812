

#此示例示意打开一个文件，同时对文件的内容进行读取操作
try:
    f = open("myfile.txt",'r',encoding='utf-8')
    print("文件打开成功")
    #2.读取文件
    s = f.read()
    print("读取的字符个数是：",len(s))
    print("文件的内容是：",s)
    #3，关闭文件
    f.close()
    print("文件关闭成功")
except OSError:
    print("打开文件失败！！！")





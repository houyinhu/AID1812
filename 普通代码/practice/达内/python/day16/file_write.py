
#此示例示意文件的基本操作
#请打开文件
try:
    f = open("mynote.txt",'w',encoding='utf-8')
    #写文件
    #只能写字符串
    f.write("abcd\n")
    f.write("你好\n")
    f.writelines(["abcd",'1234'])
    #关闭文件
    f.close()
except ValueError:
    print("打开文件失败")











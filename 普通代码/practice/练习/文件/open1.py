
try :
    file = open("while.txt",'r',encoding='utf-8')
    print("文件已经打开")
    s=file.read()
    print(s)
    file.close()
except OSError:
    print("打开文件失败")


# try:
#     file = open("/etc/passwd")
#     print("文件已经打开...")
#     s = file.readline()
#     print(s , end='')
#     file.close()
# except IOError:
#     print("打开文件失败：")



# writelines方法
# f.writelines(lines)
# lines为字符串列表（文本文件）或字节串列表（二进制）
# try:
#     f = open("test.txt",'w')
#     f.writelines(['hello',' ','world!'])
#     f.writable()
#     f.close()
# except:
#     print("打开操作失败！")



# write方法
# f.write(data)
# data为字符串（文本文件）或字节串（二进制文件）
# try:
#     f = open('test1.txt','w')
#     f.write('hello worle!')
#     f.close()
# except:
#     print("打开操作失败！")

# tell方法
# F.tell()
# try:
#     f = open('test.txt','rb')
#     b = f.read(3)
#     b = f.read(5)
#     r = f.tell()
#     print("当前的读写位置是：",r)
# except:
#     print("打开操作失败！")


# seek方法
# 改变数据流读写指针的位置，返回新的绝对位置








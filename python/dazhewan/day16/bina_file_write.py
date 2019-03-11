
#此示例示意写入256个字节到一个文件中
#第一个字节为值为0，第二个字节的值为1.。。依次类推

try:
    f = open('myfile.bin','wb') #'wb'为二进制写操作
    b = bytes(range(256))   #创建一个256的字节串
    print(b)
    f.write(b)  #写入的256个字节到文件中
    print("成功写入的",'个字节')  #注f.write()返回值为写入的字节数

    f.close()
except OSError:
    print("文件打开失败")







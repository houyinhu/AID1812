

# 练习1：
# 现有字符串s = 'Welcome to 中国'，请将其转化为编码为'gbk'的字节串，并打印其内容
# 现有字节串b = b'Python\xe7\x89\x9bX'，请将其转化为字符串，并打印其内容

# s = 'Welcome to 中国'
# b = b'Python\xe7\x89\x9bX'
#
# print(s.encode(encoding='gbk'))
# print(b.decode())


# 练习2：
# 现有字符串：s2 = 'HelloTarena'，请完成以下操作
# (1).以w+b方式打开文件'tarena.txt'，并将s2写入到tarena.txt中
# (2).返回’tarena.txt'中文件流的绝对位置
# (3).改变数据流的位置：从头开始向后0个字节  # seek()
# (4).读取5个字节，查看运行结果
# (5).返回当前文件流的绝对位置


s2 = 'HelloTarena'

with open('tarena.txt','w+b') as f1:
    f1.write(s2.encode(encoding='utf-8'))
    print(f1.tell())
    f1.seek(0,0)
    print(f1.tell())
    print(f1.read(5))
    print(f1.tell())
















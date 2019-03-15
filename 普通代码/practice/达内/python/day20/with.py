#with.py

try:
    f = open('a.txt','rt')
    for line in f:
        print(line)
except:
    print("文件操作失败")
finally:
    try:
        f.close()   #关闭文件
    except:
        print('关闭文件失败')


try:
    #使用with语句，不管以下的操作是否发生异常，都能保证文件被正确关闭
    with open('a.txt','rt') as f:
        for line in f:
            print(line)
except:
    print("文件操作失败")











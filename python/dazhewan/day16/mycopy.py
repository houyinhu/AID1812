


def copy_file():
    try:
        file1 = input("请输入源文件")
        file2 = input("请输入目标文件")
        f1 = open(file1,'rb')
        f2 = open(file2,'xb')
        f1s=f1.read(4096)
        f2.write(f1s)
        print("复制文件成功")
        f1.close()
        f2.close()
    except OSError:
        print("打开文件失败")
copy_file()









string=input("请输入")
print("第一个字符是",string[0])
print("最后一个字符是",string[-1])
if len(string)%2==0:
    pass
else:
    a=len(string)
    print(string[a//2])
#  输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
str1=input("请输入一行字符")
zimu=0
kongge=0
shuzi=0
qita=0
for i in range(0,len(str1)):
    c=str1[i]
    if c.isspace():
        kongge+=1
        continue
    if c.isalpha():
        zimu+=1
    if c.isdigit():
        shuzi+=1
    else:
        qita+=1
print("字母有",zimu)
print("空格有",kongge)
print("数字有",shuzi)
print("其他有",qita)
        




s=input("请输入字符串")
#统计字符的个数
#如果第一次出现这个字符
#    用这个字符创建字典的建，值为1
#  如果第二次或之后出现这个字符，直接将建对应的值加1
d=dict()
for x in s:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
print('d=',d)
for k in d:
    print("字符",k,':',d[k],'次')

d1=dict()
for i in s:
    
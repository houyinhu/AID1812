str1=input("请输入字符串")
i=1
while i<=len(str1):   
    print(str1[-i])
    i+=1
print('----------')
j=len(str1)-1
while j >=0:
    print(str1[j])
    j-=1
print('----------')
for c in str1[::-1]:
    print(c)

str1=input("请输入一段字符串")
count=0
for i  in  str1:
    if i == ' ':
        count+=1
print(count)

count1=0
for j in str1:
    if 64<ord(j)<91 or 96<ord(j)<123:
        count1+=1
print('英文字母的个数为',count1)

i=0
count3=0
while i<len(str1):
    if str1[i]==' ':
        count3+=1
    i +=1
print("空格的个数为:",count3)

string=input("请输入")
a=len(string)-1
string1=string[1:a]
print(string1)

if string[::-1]==string:
    print("是回文")
else:
    print("不是回文")
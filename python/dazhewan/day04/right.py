a=input("请输入")
b=input("请输入")
c=input("请输入")
print('%20s'%a)
print('%20s'%b)
print('%20s'%c)
#左侧手动添加空格
#求三个字符串的最大长度，用max函数实现
#max_len=max(len(a),len(b),len(c))
max_len=len(a)
if len(b)>max_len:
    max_len=len(b)
if len(c)>max_len:
    max_len=len(c)
print(" "*(max_len-len(a))+a)
print(" "*(max_len-len(b))+b)
print(" "*(max_len-len(c))+c)
#方法二，很据最长额字符串长度max_len来生成相应的格式化字符串
#如max_len 绑定10,则生成‘%10s’
fmt="%"+str(max_len)+"s"
print("fmt=",fmt)
print(fmt%a)
print(fmt%b)
print(fmt%c)
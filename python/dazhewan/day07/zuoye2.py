# 输入一些单词和解释，将单词作为键，键解释作为值，存入字典中当
# 输入单词或解释为空是停止输入，并打印这个字典
# 然后，输入查询的单词，给出单词的内容，如果单词不存在则提示，
# 查无此词
d={}
while True:
    d1=input("请输入单词")
    if d1=='':
        break
    d2=input("请输入解释")
    if d1=='' :
        break
    d[d1]=d2
print(d)
n=input("请输入查询的单词")
if n in d:
    print(d[n])
else:
    print("查无此词")





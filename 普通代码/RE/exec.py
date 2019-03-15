import re

f = open('test')
data = f.read()

#大写字母开头单词
pattern1 = r'\b[A-Z]\S*?\b'

#数字
pattern2 = r'-?\d+\.?/?\d*%?'

#日期格式替换
pattern3 = r'\d{4}-\d{1,2}-\d{1,2}'

# regex = re.compile(pattern2)
# for i in regex.finditer(data):
#     print(i.group())

regex = re.compile(pattern3)
for i in regex.finditer(data):
    s = i.group()
    print(re.sub(r'-','.',s))

f.close()
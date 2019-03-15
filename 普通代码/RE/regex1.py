import re

pattern = r'\d+'
s = '2019年4月28日'

it = re.finditer(pattern,s)
# # print(dir(next(it)))
for x in it:
    print(x.group())

#完全匹配
try:
    obj = re.fullmatch(r'\w+','hello_1973')
    print(obj)
    print(obj.group())
except AttributeError:
    pass

#匹配开始位置
obj = re.match(r'[A-Z]\w+','Hello World')
print(obj.group())

#匹配第一个
obj = re.search(r'\d+','2018年12月24日')
print(obj.group())

import re

regex = re.compile(r'\w+')
l = regex.findall('Welcome to 北京 ')
print(l)

regex = re.compile(r'\w+',flags=re.A)
l = regex.findall('Welcome to 北京 ')
print(l)
print('--------------------------------------')

#忽略字母大小写
regex = re.compile(r'[a-z]+')
l = regex.findall('Welcome to 北京 ')
print(l)

regex = re.compile(r'[a-z]+',flags=re.I)
l = regex.findall('Welcome to 北京 ')
print(l)
print('--------------------------------------')
#.可以匹配换行
regex = re.compile(r'.+')
l = regex.findall('Welcome to \n 北京 ')
print(l)

regex = re.compile(r'.+',flags=re.S)
l = regex.findall('Welcome to \n 北京 ')
print(l)
print('--------------------------------------')
regex = re.compile(r'^北京')
s = '''Welcome to
北京
'''
l = regex.findall(s)
print(l)

regex = re.compile(r'^北京',flags=re.M)
s = '''Welcome to
北京
'''
l = regex.findall(s)
print(l)

print('--------------------------------------')

#为正则表达式添加注释
pattern = r'''[A-Z][a-z]*
\s+\w+\s+#匹配空行和第二个单词
\w+
'''
regex = re.compile(pattern,re.X)
s = '''Welcome to
北京
'''
l = regex.findall(s)
print(l)

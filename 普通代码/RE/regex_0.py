
from re import compile

pattern = r'(ab)c(de)'
regex = compile(pattern,flags=0)
a = regex.findall('abcdef')
print(a)


pattern = r'\s+'
regex = compile(pattern,flags=0)
a = regex.split('hello  world nihao')
print(a)

pattern = r'垃圾'
regex = compile(pattern)
a = regex.sub('**','你真垃圾')
print(a)

pattern = r'垃圾'
regex = compile(pattern)
a = regex.subn('**','你真垃圾,垃圾，垃圾',2)
print(a)

pattern = r'ab'
regex = compile(pattern)
a = regex.finditer('abcdab')
for x in a:
    print(x.group())

pattern = r'cd'
regex = compile(pattern)
try:
    a = regex.fullmatch('cdf')
    print(a.group())
except AttributeError:
    pass

pattern = r'hello'
regex = compile(pattern)
a = regex.match('hello world')
print(a.group())


pattern = r'hel'
regex = compile(pattern)
a = regex.search('hello world')
print(a.group())






# 1，随机生成6为密码：
# 可以作为密码的字符有：
# a-z,A-Z,0-9
# 随机生成一个6位的密码

import random

# def password():
#     i=0
#     while i<6:
#         a=chr(random.randint(ord('a'), ord('z')))
#         b=chr(random.randint(ord('A'),ord('Z')))
#         c=random.randint(0,9)
#         l=[a,b,c]
#         print(random.choice(l),end='')
#         i+=1
# password()

#老师做法
charator = [chr(ch) for ch in range(65,65+26)]
charator += [chr(ch) for ch in range(97,97+26)]
charator += [chr(ch) for ch in range(48,48+10)]
passwd = ''
for _ in range(6):
    passwd += random.choice(charator)
print("密码是：",passwd)







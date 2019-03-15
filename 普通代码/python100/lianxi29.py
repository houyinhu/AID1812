
# 题目：给一个不多于5位的正整数，要求：一、求它是几位数
# ，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

# a=454
#
# a1=str(a)
# la=len(a1)
# print(a,"是",la,'位数')
#
# a2=a1[::-1]
# a3=int(a2)
# print("反过来是",a3)


# b='12321'
# if  b[::-1] == b:
#     print("是回文数")
# else:
#     print("不是回文数")

l=['1','2','2']
a='/'.join(str(x) for x in l)
print(a)
# s='a sd f'
# s1=s.split(' ')
# print(s1)

l1=[1,2,4,5,6,3,4]
l1s=','.join(str(x) for x in l1)
print(l1s)









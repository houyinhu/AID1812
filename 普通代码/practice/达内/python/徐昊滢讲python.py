
# 列表：
#     可以被改变的序列
# l=[1,2]
# print(id(l))
# l+=[3]
# print(id(l))
#
# l1=list(range(10))
# print(l1)


# s='hello world python'
# l1=list(s)
# print(l1)
# l=s.split()
# print(l)

# l3=['2019','12','1']
# s1=' '.join(l3)
# print(s1)

#
# l1=[1,2,[3,4]]
# l2=l1
# l3=l1.copy()
# import copy
# l4=copy.deepcopy(l1)
# l1[0]=6
# l1[2][0]='a'
# print('l1:',l1)
# print('l2:',l2)
# print('l3:',l3)
# print('l4:',l4)

# 元组
    #不可变的列表

# l=[3,4]
# print(id(l))
# t=(1,2,l)
# print(id(t))
# t[2][0]='a'
# print('t:',id(t))
# print('l:',id(l))
# print(t)
# print(l)

#字典 dict
    #无序的可变的容器
    #键必须是不可变的,唯一  哈希
# L=[1,2]
# print(id(L))
# L=[1,2,3]
# print(id(L))
# d={}

d=dict([(1,"一"),(2,'二')])
d1=dict(name='xiaozhang',age=20,score=100)
print(d)
print(d1)



#集合
    #可变的 无序的容器
    #里面的元素不可变，唯一
# s=set()
# print(s)



#固定的集合 不可变的 无序
# s=frozenset()
# print(s)
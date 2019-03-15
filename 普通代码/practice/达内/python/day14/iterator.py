

L=[2,3,5,7]
#如何遍历L中的数据

#方法一
# i=0
# while i < len(L):
#     x=L[i]
#     print(x)
#     i +=1

#方法二
# for x in L:
#     print(x)

#方法三 用迭代器来遍历

it=iter(L)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break



# L=[2,3,5,7]
# it = iter(L)		#it 绑定一个能访问L列表的迭代器
# print(next(it))	#通过it	从可迭代对象中提取一个数据
# print(next(it))
# print(next(it))
# print(next(it))

#访问range
# it = iter(range(1,10,3))
# print(next(it)) #1
# print(next(it)) #4
# print(next(it)) #7
# print(next(it)) #StopIteration

# while True:
#     try:
#         print(next())
#     except StopIteration:
#         print("访问器结束")
#         break










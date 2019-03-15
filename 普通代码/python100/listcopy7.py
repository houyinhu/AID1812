# 题目：将一个列表的数据复制到另一个列表中。

# 程序分析：使用列表[:]。
list1=[1,2,3,4,5,6,4]
list2=list1.copy()
list3=list1[:]
list4=list1
print(list1)
print(list2)
print(list3)
print(list4)
list1=[2,5,7,4,6,4]
print(list1)
print(list2)
print(list3)
print(list4)
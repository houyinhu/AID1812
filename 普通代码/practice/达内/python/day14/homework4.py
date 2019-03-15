
# 打印杨辉三角，只打印6层
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#  1 5 10 10 5 1
# n=int(input("请输入杨辉三角的层数"))
# xiao=[]
# for x in range(0,n):
#     da=[1]
#     print(" "*(n-x-1),end='')
#     for y in range(0,x):
#         if y == x-1:
#             da.append(1)
#         else:
#             da.append(xiao[y]+xiao[y+1])
#     for j in da:
#         print(j,end=' ')
#     xiao=da
#     print()

#老师做法
def get_next_line(L):
    #此函数根据上一层L， 返回下一层数字列表
    #如L = [1,2,1]
    #返回[1,3,3,1]
    #最左边的1
    L2 = [1]
    #计算中间的数字
    for i in range(len(L)-1):
        L2.append(L[i] +L[i+1])
    #添加最后一个1
    L2.append(1)
    return L2
def get_yanghui_list(n):
    #此函数返回n层的杨辉三角的列表
    #如 n 等于3 则返回
    [
        [1],
        [1,1],
        [1,2,3],
        [1,3,3,1]
    ]
    L = []#用来存放每一层的列表
    layer = [1]
    while len(L)<n:
        #每次循环放入一层
        L.append(layer)
        layer = get_next_line(layer)#算出下一层
    return L
def get_yanghui_string_list(L):
    #此函数 传入一个有数字列表组成的列表 返回字符串列表
    #如[[1], [1, 1], [1, 2, 1]]
    #返回['1','1 1','1 2 1']
    L2 = []#准备存放字符串
    for layer in L:
        s = ' '.join((str(x) for x in layer))
        L2.append(s)
    return L2

def print_yanghui_triangle(L):
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))

# print(get_yanghui_list(6))
L=get_yanghui_list(6)
string_L = get_yanghui_string_list(L)
print(print_yanghui_triangle(string_L))

# print(get_next_line([1]))
# print(get_next_line([1,1]))





# for i in range(1,n+1):  #控制行数
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):  #控制每列上的数字
#
#         if j==1 or j ==i:
#             ret.append[1]
#             print(("%2d" % 1), end='')
#         if j >1 and j !=i:
#
#             print(("%2d"%j),end='')
#     if i>3:
#

# n=int(input("请输入杨辉三角的层数"))
# start=[1]
# for i in range(0,n):  #控制行数
#     print(' '*(n-i),end='')
#     for j in range(0,i):  #控制每列上的数字
#
#         if j==0 or j ==i-1:
#             start.append[1]
#         start[j] = start[j - 1] + start[j]
#         start.append(start[j])
#
#             print(("%2d"%j),end='')
#     finally=start[:]
#     print(finally)
# start=[1]
# L=[1]
# L=[1,1]
# L=[1,2,1]
# L=[1,3,3,1]
# L=[1,4,6,4,1]   l[0] L[i-1] =1 L[j]=L[j-1]+L[j] 0-i
# start[j]=start[j-1]+start[j]
# start.append
# finally=start[:]












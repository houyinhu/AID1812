# 2, 已知有列表：
# L = [[3, 5, 8], 10, [[12, 14], 15, 18], 20]
# 1)写一个函数
# print_list(lst)
# 打印出所有的数字
# 如：
# 2）写一个函数，sum_list(lst)
# 返回这个列表中所有数字的和：
# 如：
# print(sum_list(lst))
# # 打印106
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

def print_list(lst):
    for x in lst:
        if type(x) is list:#如果是列表，则按相同的规则打印列表
            print_list(x)
        if type(x) is int:#如果是字符串则打印字符串
            print(x,end=' ')
print_list(L)

sum1=0
def sum_list(lst):
    global sum1
    for x in lst:
        if type(x) is list: #如果是列表，则按相同的规则循环
            sum_list(x)
        if type(x) is int:#如果是字符串则相加
            sum1+=x
    return sum1
print(sum_list(L))


def sum_list(lst):
    sum1=0
    for x in lst:
        if type(x) is list: #如果是列表，则按相同的规则循环
            sum1+=sum_list(x)
        if type(x) is int:#如果是字符串则相加
            sum1+=x
    return sum1
print(sum_list(L))










# 2. 分解质因数, 输入一个正整数,分解质因数,
#     如:
#       输入: 90
#     则打印:
#       '90=2*3*3*5'
#       (质因数是指最小能被原数整除的素数(不包括1))

# number1 = int(input("请输入一个整数"))
# print(number1,'=',end='')
# for x in range(2,number1+1):
#     while number1!=x:
#         if number1%x ==0:
#             print(x,'*',end='')
#             number1/=x
#         else:
#             break
# print("%d"%number1,end=' ')

def get_zhiyin_list(x):
    #此函数返回x的质因数的列表
    #x=90 返回[2,3,3,5]
    L=[] #准备存放质因数
    while x>1:
        #每次求取一个质因数，然后放入L中
        for i in range(2,x+1):
            if x %i == 0:#i一定是质因数
                L.append(i)
                x = int(x/i)
                break
    return L
x = int(input("请输入正整数:"))
L=get_zhiyin_list(x)
L2=(str(x) for x in L)
print(x, '=','*'.join(L2))







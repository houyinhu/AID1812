num1=int(input("请输入宽"))
#num2=int(input("请输入高"))
stars=1 #start代表星号的个数，也是行数
while stars<=num1:
    print('*'*stars)
    stars+=1
print('---------') 
stars=1
while stars <= num1:
    #计算出左侧空格的个数
    blank=num1-stars
    print(' '*blank+'*'*sanrs)
    satrs+=1
stars=1
print("-------------")
stars=num1
while stars>0:
    stars-=1
    blank=num1-stars
    print(' '*blank+"*"satrs)
print("-------------")
stars=num1
while stars>0:
    pirnt("*"*satrs)
    stars-=1















# i=1
# while 
# while i<=num1:
#     while i<=num1:
#         print('*'*i,end=' ')
#         print()
#         i+=1
#     print('------------')
#     while j<=num1:
#         pritn(' '*j,)



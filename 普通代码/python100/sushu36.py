

# xiao = int(input("请输入最小区间"))
# da = int(input("请输入最大区间"))
#
# for num in range(xiao,da+1):
#     for x in range(2,num):
#         if  num%x ==0:
#             break
#     else:
#         print(num)


a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
a.sort()
last=a[-1]
for i in range(len(a)-2,-1,-1):
    if last==i:
        del i
    else:last=i
print(a)




l=[1,2,3,1,6,4,1,2,4,523,41,41,124,51,5,1512,5,5325,36,34,98,82]
# l2=[]
# l3=[]
# for i in l:
#     c=l.count(i)
#     if c ==2 and i not in l3:
#         l3+=[i]
#     if  i not in l2:
#         l2+=[i]
# print("新的列表为",l2)
# print("出现两次的为",l3) 
l2=l[:]
l3=[]
for i in l:
    n=l2.count(i)#x在l2中的个数
    m=l.count(i)#x在l3中的个数
    if m==2:
        
        l3.append(i)
        
    while n>1:
        l2.remove(i)
        n-=1
print(l2)
print(set(l3))







        



l=[]
count=0
n=0
while True:
    w=input("请输入")
    l+=[w]
    count+=len(w)
    if w=='':
        break
    n+=1
for i in range(len(l)):
    print(l[i])
print("wenzi",count)
print("hang",n)




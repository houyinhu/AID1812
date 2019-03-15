

a=[1,2,5,7,6,3,4]

for x in range(len(a)):
    for y in range(x+1,len(a)):
        if x+1 == len(a):
            break
        else:
            if a[x] < a[y]:
                pass
            else:
                a1=a[x]
                a[x] = a[y]
                a[y] = a1
print(a)













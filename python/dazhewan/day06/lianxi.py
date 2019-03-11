print("a",end='')
print('b',end='')
i=1
count=0
while i <=10:
    j=1
    while j <=10:
        if j == 5:
            break
        count+=1
        j+=1
    i+=1
    print(count)

print(r"Newlines are indicated by \n")

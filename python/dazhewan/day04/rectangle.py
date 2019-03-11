n=int(input('请输入矩形宽度'))
count=0
while count<n:
    if count==0 or count==n-1:
        print('#'*n)
        count+=1
    else:
        print('#',' '*(n-4),'#')
        count+=1

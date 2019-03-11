


def myeven(begin,end):

    while begin < end:
        if begin%2 == 0:
            yield begin
        begin +=1
for x in myeven(1,10):
    print(x)
L = [x**2 for x in myeven(4,9)]
print(L)





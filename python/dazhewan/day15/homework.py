

def myxrange(start,stop='',step=1):
    if start<0 and stop=='':
        pass
    if stop=='':
        i=0
        while start>0:
            yield i
            i+=1
            start-=1
    else:
        while start<stop:
            yield start
            start+=step


# print(sum(x**2 for x in myxrange(1,10) if x%2))







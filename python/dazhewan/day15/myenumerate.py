


# def myenumerate(iterable,start=0):
#     it1 = iter(iterable)    #拿到迭代器
#     while True:
#         try:
#             yield start,next(it1)
#             start+=1
#         except StopIteration:
#             return

#方法二
def myenumerate(iterable,start=0):
    for v in iterable:
        yield start,v
        start+=1


L = [3,5,8,10]
for x,y in myenumerate(L):
    print(x,y)














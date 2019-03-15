

# def goodbye(L):
#     for x in L:
#         print("再见:",x)
#
# def operator(fn,L):
#     fn(L)
#
# operator(goodbye,['Tom','Jerry','Spike'])

def myinput(fn):
    L = [1,3,5,7,9]
    return fn(L)
print(myinput(max))
print(myinput(min))
print(myinput(sum))









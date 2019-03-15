

#生成一个可迭代对象，此可迭代对象可以生成
#   1**4    2**3    3**2    4**1

# y = 4
# for x in range(1,5):
#     print(x**y)
#     y-=1

# for x in  map(pow,[1,2,3,4],[4,3,2,1]):
#     print(x)
print("------------")
for x in map(pow,[1,2,3,4],[4,3,2,1,0],range(5,10)):
    print(x)


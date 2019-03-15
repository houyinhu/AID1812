# 练习：
#     1，一个球从100米高空落下，每次落地后反弹高度为原高度的一般，在落下，写程序算出“
#         1）皮球在第10此落地后反弹的高度
#         2）皮球在第10此落地反弹后共经历多少米路程

# height = 100
# i=0
# s=100
# while i<10:
#     height*=0.5
#     i+=1
#     s+=2*height
# print('第十次的反弹的高度为：',height)
# print('第十次的反弹共经历了：',s)

def get_last_height(height,times):
    for _ in range(times):
        height /=2
    return height
def get_distance(height,times):
    meter = 0 #用来记录总路程
    for _ in range(times):
        #累加下落过程的路程
        meter+=height
        height /=2
        meter +=height
    return meter
print("皮球从100米高度落下反弹十次后高度为",get_last_height(100,10))
print("皮球从100米高度落下反弹十次后总路程为",get_distance(100,10))







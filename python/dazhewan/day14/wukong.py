
s = {'唐僧' ,'悟空' ,'八戒' ,'沙和尚'}
#
# for x in s :
#     print(x)
# else:
#     print("遍历结束")

it = iter(s)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        print("遍历结束")
        break





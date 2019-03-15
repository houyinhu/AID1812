


def get_score():
    try:
        number=int(input("请输入 1~100的整数"))
    except ValueError as a:
        print(a)
        return 0
    except :
        print("发生未知错误")
        return 0
    else:
        print("没有发生异常")
    if number < 0 or number > 100:
        return 0
score=get_score()
print("学生成绩是：",score)


#老师的做法
# def get_score():
#     try:
#         number=int(input("请输入 1~100的整数"))
#         if number<0 or number>100:
#             return 0
#         return number
# try:
#     score = get_score()
# except ValueError:
#     score=0
# print("学生成绩是：",score)





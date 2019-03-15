
#此示例示意用raise语句来传递信息给调用者

#当用户输入的数字不是0~100之间的数时，用异常方式通知调用者

def get_score():
    '''此函数强制用户输入0~100之间的数，如果输入的是其他的数则直接触发异常来通知调用者'''
    score = int(input("请输入成绩："))
    if score<0:
        raise  ValueError("成绩小于最小值")
    if score>100:
        raise ValueError("成绩超出了最大值")
    return score
try:
    score = 0
    print("学生的成绩是：",score)
except ValueError as err:
    print("用户输入有错",err)
score = get_score()













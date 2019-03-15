#让程序输入一个学生的成绩（0-100）之间 如果不在这个
#范围则报错
score=int(input(""))
if 0<=score<=100:
    #print("成绩合法")
    pass
else:
    print("成绩不合法，输入有错")
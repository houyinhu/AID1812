

# 练习1：
# Python调试器需要导入什么模块，模块中的方法是什么？
# 在控制台下运行调试器的命令格式


# 写一个程序student_info.py要求运行时实现如下功能：
# $ python3 student_info.py
# 请输入姓名：
# 请输入年龄：(将年龄转化为int类型)
# 请输入成绩：(将成绩转化为int类型)
#
# 要求： 如果学生年龄和成绩输入有错误，则打印："输入有误，请重新输入学生信息！"
# 然后让用户重新输入姓名、年龄、及成绩

while True:
    try:
        a1 = input("请输入姓名：")
        a2 = int(input("请输入年龄"))
        a3 = int(input("请输入成绩"))
    except KeyboardInterrupt:
        print("程序退出！")
        break

    except:
        print("输入有误，请重新输入")


# 练习3：
# 在练习2中的student_info.py中添加语句，实现用户在
# 输入 ctrl + c终止程序时直接终止程序但不会报错




















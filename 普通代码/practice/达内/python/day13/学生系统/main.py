from menu import show_menu
import student_infof
def main():
    L=[]
    # 此列表储存学生信息# 创建一个列表，准备存放学生数据的字典
    while True:
        show_menu()
        s = input("请输入你的操作")
        try:
            if s == '1':
                student_infof.add_information(L)
            elif s == '2':
                student_infof.output_student(L)
            elif s == '3':
                student_infof.delete_student(L)
            elif s == '4':
                student_infof.modify_score(L)
            elif s == '5':
                 student_infof.scoresheng(L)
            elif s == '6':
                student_infof.scorejiang(L)
            elif s == '7':
                student_infof.agesheng(L)
            elif s == '8':
                student_infof.agejiang(L)
            elif s == 'q':
                break
        except:
            print("输入错误")
main()





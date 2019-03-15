
# def build_person(first_name,last_name,age=''):
#     #返回一个字典，其中包含有关一个人的信息
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#     return person
# musician=build_person('jimi','hendrix',age=27)
# print(musician)
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\n Please tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name=input(("First name:"))
    if f_name=='q':
        break
    l_name = input(("Last name:"))
    if l_name == 'q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello,"+formatted_name+'!')

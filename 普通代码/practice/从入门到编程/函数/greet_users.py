# 用函数来提高处理列表的效率。

# 假设有一个用户列表，我们要问候其中的每位用户。下面的示例将一个名字列表传递给一个
# 名为greet_users()的函数，这个函数问候列表中的每个人
def greet_users(names):
    # 向列表中的每位用户都发出简单的问候
    for name in names:
        msg="hello,"+name.title()+'!'
        print(msg)
usernames=['hannag','ty','margot']
greet_users(usernames)





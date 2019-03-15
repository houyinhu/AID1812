
# 10-8 猫和狗：创建两个文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的
# 名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并
# 将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存
# 在时捕获 FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地

with open('dogs.txt') as file_object:
    for i in file_object:
        print(i.rsplit())












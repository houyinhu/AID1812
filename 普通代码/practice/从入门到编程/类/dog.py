

class  Dog():
    #依次模拟小狗的签单尝试
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def  sit(self):
        #模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        #模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!")

my_dog = Dog('wille',6)
#但Python自动返回一个表示这条小狗的实例。我们将这个实例存储在变量my_dog中

your_dog=Dog('lucy',3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " +your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + "years old .")

your_dog.sit()













# 练习1：
class Student:
	def __init__(self,name,age,score):
		self.name,self.age,self.score = name,age,score
	def __repr__(self):
		return "Hello world"
	def infos(self):
		m = "Hello China"
		print(m)
	# def __str__(self):
	# 	return self.infos()

s1 = Student("Bob",30,88)
print(s1)
# 请问执行结果是什么？理解其中的原因













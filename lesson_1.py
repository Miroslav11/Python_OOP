class Student:

	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age


lucija = Student('Lucija', 88, 22)
mario = Student('Mario', 83, 19)

print(lucija.name)
print(mario.name)

print(lucija.grade)
print(mario.grade)

print(lucija.age)
print(mario.age)
class Animal:
	def __init__(self, name, like_to_eat, like_to_do, in_love):
		self.name = name
		self.eat = like_to_eat
		self.do = like_to_do
		self.love = in_love

	def __str__(self):
		return "{} likes to eat {}, likes to {} and he is in love in {}".format(self.name, self.eat, self.do, self.love)



class Dog(Animal):
	def talk(self):
		return "WOOF-WOOF!!!"

pet_dog = Dog("Riki", "bones", "chasing own tail", "Jessica")	# represents attributes from the dunder method "__init__" form the class "Animal"

print(pet_dog)			# printing attributes from the class "Animal"
print(pet_dog.talk())	# printing from the class "Dog"
print()					# just to make space between print methods



class Bull(Animal):
	def talk(self):
		return "MUUUUUU!!!"

bull = Bull("Alejandro", "grass", "chasing red flag", "Missy")

print(bull)
print(bull.talk())
class Fighter: # "Fighter" is the class name

	def __init__(self, name):
	# "__init__" is the dunder (double underscore) method (function inside of class is called method)
		self.name = name # ".name" (after "self") is attribute
		self.health = 100
		self.damage = 10
		self.destroy = 30


	def attack(self, other_guy): 
	# "attack" is the method (function inside of class is called method)
	# "other_guy" is input parameter or argument ("self" is not a argument).
		other_guy.health = other_guy.health - self.damage
		if other_guy.health <= 0:
			print("{} attacks {}".format(self.name, other_guy.name)) # string formating
			print("{} now has 0 points".format(other_guy.name))
			print ("{} LOST!!!".format(other_guy.name))
		else:
			print("{} attacks {}".format(self.name, other_guy.name))
			print("{} now has {} points".format(other_guy.name, other_guy.health))


	def smash(self, other_guy):
		other_guy.health = other_guy.health - self.destroy
		if other_guy.health <= 0:
			print("{} smash {}".format(self.name, other_guy.name))
			print("YOU'VE BEEN SMASHED!!!")
			print("{} now has 0 points".format(other_guy.name))
			print("{} LOST!!!".format(other_guy.name))
		else:
			print("{} smash {}".format(self.name, other_guy.name))
			print("YOU'VE BEEN SMASHED!!!")
			print("{} now has {} points".format(other_guy.name, other_guy.health))


	def __str__(self):
	# "__str__" is the dunder method who overrides certain function, in this case "print" method
		return "{} : {}".format(self.name, self.health)



chopsocky = Fighter("Chopsocky") # "chopsocky" is the object created from the class "Fighter"
western = Fighter("Spaghetti Western")


print(chopsocky)
print(western)
print()
chopsocky.attack(western)
print()
western.attack(chopsocky)
print()
chopsocky.attack(western)
print()
chopsocky.attack(western)
print()
western.attack(chopsocky)
print()
chopsocky.smash(western)
print()
chopsocky.smash(western)
print()
western.smash(chopsocky)
print()
chopsocky.smash(western)
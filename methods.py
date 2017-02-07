class Fighter:

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

	def attack(self, other_guy):
		other_guy.health = other_guy.health - self.damage
		print("{} attacks {}".format(self.name, other_guy.name))
		print("{} have now {} points".format(other_guy.name, other_guy.health))

	def __str__(self):
		return "{} : {}".format(self.name, self.health)

miro = Fighter("Miro")
marko = Fighter("Marko")

print(miro)
print(marko)

miro.attack(marko)
print()
marko.attack(miro)
print()
miro.attack(marko)
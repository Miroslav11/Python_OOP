# Chicken and the egg
# Haha, this is not the endless debate about which came first :)

class Chicken:
	def __init__(self, chicken_name, eggs_amount):
		self.chicken_name = chicken_name
		self.eggs_amount = eggs_amount

	def lays_egg(self, lays_egg_amount):
		self.lays_egg_amount = lays_egg_amount
		print("{} layed {} eggs".format(self.chicken_name, self.lays_egg_amount))		# How many eggs Helen layed
		self.eggs_amount += lays_egg_amount
		

	def pick_egg(self, pick_egg_amount):
		self.pick_egg_amount = pick_egg_amount
		print("You pick {} eggs".format(self.pick_egg_amount))							# How many eggs you've picked
		self.eggs_amount -= pick_egg_amount
		print("{} now has {} eggs".format(self.chicken_name, self.eggs_amount))			# How many eggs Helen now has



chicken = Chicken("Helen", 0)


chicken.lays_egg(7)
chicken.pick_egg(3)
chicken.lays_egg(2)
chicken.pick_egg(4)
print("Helen is angry, and I\'m hungry")
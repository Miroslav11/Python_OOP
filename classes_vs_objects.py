class Worker: # "Worker" is the class name

	def __init__(self, name, age, address, hometown):
	# "__init__" is the method (function inside of class is called method)
	# example: def learn(self, ...)... "learn" is the method. "name, age,...." are input parameters or arguments (self is not a argument).
		self.name = name # ".name" (after "self") is attribute
		self.age = age
		self.address = address
		self.hometown = hometown

ivan = Worker('Ivan,', '28 years,', 'Blueberry Street 36,', 'Utopia.') # "ivan" is the object created from the class "Worker"
josip = Worker('Josip,', '36 years,', 'Yellowlight Street 136,', 'Oz.')
miro = Worker('Miro,', '38 years,', 'Color Street 1,', 'Dreamland Town.')
blondie = Worker('Marijana,', '24 years,', 'Strawberry Street 95,', 'Bluetown.')

print(ivan.name, ivan.age, ivan.address, ivan.hometown)
print(josip.name, josip.age, josip.address, josip.hometown)
print(miro.name, miro.age, miro.address, miro.hometown)
print(blondie.name, blondie.age, blondie.address, blondie.hometown)
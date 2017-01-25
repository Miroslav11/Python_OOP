class Workers:

	def __init__(self, name, age, address, hometown):
		self.name = name
		self.age = age
		self.address = address
		self.hometown = hometown

ivan = Workers('Ivan,', '28 years,', 'Blueberry Street 36,', 'Utopia.')
josip = Workers('Josip,', '36 years,', 'Yellowlight Street 136,', 'Oz.')
miro = Workers('Miro,', '38 years,', 'Color Street 1,', 'Dreamland Town.')
blondie = Workers('Blondie,', '24 years,', 'Strawberry Street 95,', 'Bluetown.')

print(ivan.name, ivan.age, ivan.address, ivan.hometown)
print(josip.name, josip.age, josip.address, josip.hometown)
print(miro.name, miro.age, miro.address, miro.hometown)
print(blondie.name, blondie.age, blondie.address, blondie.hometown)
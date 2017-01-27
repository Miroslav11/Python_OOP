class MusicStore:
	website_guitars = "http://sexs_drugs_rock_n_roll.com/guitars"
	website_drums = "http://sexs_drugs_rock_n_roll.com/drums"
	website_bass = "http://sexs_drugs_rock_n_roll.com/bass_guitars"

	def __init__(self, name, title, description):
		self.name = name
		self.title = title
		self.description = description

john = MusicStore('John,', 'guitar salesman,', 'guitar junkie loves to play hard :)))')
chris = MusicStore('Chris,', 'drum salesman,', 'loves drum sticks....loves any kind of sticks to punch the hole.')
kiky = MusicStore('Kiky,', 'bass salesgirl :),', 'WOMEN POWER! HATES MEN! AGRRRRR!!!')

print(john.name, john.title, john.description)
print(MusicStore.website_guitars)
print()
print(chris.name, chris.title, chris.description)
print(MusicStore.website_drums)
print()
print(kiky.name, kiky.title, kiky.description)
print(MusicStore.website_bass)
print()
print('Now I\'m going to make pizza :)')
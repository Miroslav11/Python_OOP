# fizzbuzz
# print from 1 to 100
# if number is divisible by 3 -- fizz
# if number is divisble by 5 -- buzz
# if divisible by both -- fizzbuzz

# 1
# 2
# fizz
# 4
# buzz
# ...
# fizzbuzz

# 6 divisible by 3?
# %
# 100 % 2 == 0
# print(6 % 3 == 0)
# if 7 % 3 == 0:
	# print('fizz')
'''
for number in range(1, 101):
	if number % 3 == 0:
		print('fizz')
	elif number % 5 == 0:
		print('buzz')
	elif number % 3 == 0 and number % 5 == 0:
		print('fizzbuzz')
	else:
	    print(number) 
'''
# print(number)

for number in range(1, 101):
	if number % 3 == 0 and number % 5 == 0:
		print('fizzbuz')
	elif number % 5 == 0:
		print('buzz')
	elif number % 3 == 0:
		print('fizz')
	else:
	    print(number) 



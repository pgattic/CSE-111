import random

def append_random_numbers(numbers_list, quantity = 1):
	[numbers_list.append(round(random.uniform(0, 100), 1)) for _ in range(quantity)]

def main():
	numbers = []
	append_random_numbers(numbers)
	append_random_numbers(numbers, 10)
	print(numbers)

main()

import random

my_list = []

while len(my_list) < 10:
	my_list.append(random.randint(0, 20))

my_list.sort()

print(my_list)


def my_def():
	print("yeet")

print(my_def())

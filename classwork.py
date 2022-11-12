
my_list = []

def add_to_list(target, item):
	target.append(item)
	return target

def add_to_list_at(target, item, index):
	target.insert(index, item)
	return target

def remove_from_list_at(target, index = -1):
	target.pop(index)
	return target

for i in range(0, 5):
	my_list = add_to_list(my_list, i)

print(my_list)


for i in range(0, 5):
	my_list = add_to_list_at(my_list, "h", i)

print(my_list)


for i in range(0, 5):
	my_list = remove_from_list_at(my_list, i)

print(my_list)


import json


def read():
	my_file = open("out.txt", "r")
	family_names = json.loads(my_file.read())
	return family_names


def write(family):
	print('Type "Done" to end input')
	name_input = input("Give a family member's name: ")

	while name_input != "Done":
		age_input = input(f"How old is {name_input}? ")
		family.append({"name": name_input, "age": age_input})
		name_input = input("Give a family member's name: ")

	text_file = open("out.txt", "w")

	text_file.write(json.dumps(family))

	text_file.close()
	return family


def main():
	family = read()
	
	user_input=input("what do you want to do? (w for write, p for print, e for edit, x for exit): ")
	while user_input != "x":
		if user_input == "w":
			family = write(family)
		elif user_input == "p":
			print(family)
		user_input=input("what do you want to do? (w for write, p for print, e for edit, x for exit): ")


main()

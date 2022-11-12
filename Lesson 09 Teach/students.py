import csv

students = []

def read_dict(filename):
	"""Read the contents of a CSV file into a compound
	dictionary and return the dictionary.

	Parameters
		filename: the name of the CSV file to read.
		key_column_index: the index of the column
			to use as the keys in the dictionary.
	Return: a compound dictionary that contains
		the contents of the CSV file.
	"""
	csv_file = open(filename, "r")
	output = csv.DictReader(csv_file)
	result = []
	for row in output:
		result.append(row)
	return(result)


def search_dict(the_dict, value):
	for i in the_dict:
		if i["I-Number"] == value:
			return i['Name']
	return "No such student"

def edit_dict(the_dict):
	print('Type "Done" to finish')
	new_name = input("Give a new name to add: ")
	while new_name != "Done":
		new_id = input("Gimme a student ID: ")
		the_dict.append({'I-Number': new_id, "Name": new_name})
		new_name = input("Give a new name to add: ")
	return the_dict

def write_dict(the_dict, filename):
	csv_file = open(filename, "w")
	output = csv.DictWriter(csv_file, ['I-Number', 'Name'])
	output.writeheader()
	for row in the_dict:
		output.writerow(row)

def main():
	students = read_dict("students.csv")
	print(f"found student: {search_dict(students, input('Who you lookin for?: '))}")
#	write_dict(students, "students.csv")

main()


# I-Number,Name
# 751766201,James Smith
# 751762102,Esther Einboden
# 052058203,Cassidy Benavidez
# 323021604,Joel Hatch
# 251041405,Brianna Ririe
# 001152306,Stefano Hisler
# 182706207,Hyeonbeom Park
# 124712708,Maren Thomas
# 212505409,Tyler Clark

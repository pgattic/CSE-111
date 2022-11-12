# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

gender = None
birth_date = None
weight = 0
height = 0

def main():
	# Get the user's gender, birthdate, height, and weight.
	gender = input("What is your gender? (M or F ONLY): ").lower()
	while (gender != "m") and (gender != 'f'):
		gender = input("Invalid input. What is your gender? (M or F): ").lower()
	
	# Call the compute_age, kg_from_lb, cm_from_in,
	# body_mass_index, and basal_metabolic_rate functions
	# as needed.
	age = compute_age(input("Birth Date? YYYY-MM-DD: "))
	weight = kg_from_lb(float(input("How much do you weigh? (Pounds) ")))
	height = cm_from_in(float(input("What is your height? (Inches) ")))
	bmi = body_mass_index(weight, height)
	bmr = basal_metabolic_rate(gender, weight, height, age)
	print(f"Your age: {age} years\nYour weight: {weight:.2f}kg\nYour height: {height:.2f}cm\nYour Body Mass Index: {bmi:.1f}\nYour Basal Metabolic Rate (kcal/day): {bmr:.0f}")

	# Print the results for the user to see.
	pass


def compute_age(birth_str):
	"""Compute and return a person's age in years.
	Parameter birth_str: a person's birthdate stored
		as a string in this format: YYYY-MM-DD
	Return: a person's age in years.
	"""
	# Convert a person's birthdate from a string
	# to a date object.
	birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
	today = datetime.now()

	# Compute the difference between today and the
	# person's birthdate in years.
	years = today.year - birthdate.year

	# If necessary, subtract one from the difference.
	if birthdate.month > today.month or \
		(birthdate.month == today.month and \
			birthdate.day > today.day):
		years -= 1

	return years


def kg_from_lb(pounds):
	"""Convert a mass in pounds to kilograms.
	Parameter pounds: a mass in U.S. pounds.
	Return: the mass in kilograms.
	"""
	return pounds * 0.45359237


def cm_from_in(inches):
	"""Convert a length in inches to centimeters.
	Parameter inches: a length in inches.
	Return: the length in centimeters.
	"""
	return inches * 2.54


def body_mass_index(weight, height):
	"""Compute and return a person's body mass index.
	Parameters
		weight: a person's weight in kilograms.
		height: a person's height in centimeters.
	Return: a person's body mass index.
	"""
	return (10000 * weight) / (height ** 2)


def basal_metabolic_rate(gender, weight, height, age):
	"""Compute and return a person's basal metabolic rate.
	Parameters
		weight: a person's weight in kilograms.
		height: a person's height in centimeters.
		age: a person's age in years.
	Return: a person's basal metabolic rate in kcals per day.
	"""
	bmr = 0
	match gender:
		case "m":
			bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
		case "f":
			bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
	return bmr


# Call the main function so that
# this program will start executing.
main()
import math

def compute_area(r):
	return math.pi * (r ** 2)

radius = float(input("Please enter a Radius: "))

print(f"The area is: {compute_area(radius)}")

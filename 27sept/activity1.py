import math

num_rectangles = 0
rectangles = []
rectangle_areas = []

def compute_area(w, h):
	return w*h

def append_rectangles(i):
	print(f"Rectangle #{i+1}")
	width = int(input("Width? "))
	height = int(input("Height? "))
	rectangles.append([width, height])

def append_areas(i):
	rectangle_areas.append(compute_area(rectangles[i][0], rectangles[i][1]))


def main():
	num_rectangles = int(input("How many rectangles doe??? "))
	for i in range(0, num_rectangles):
		append_rectangles(i)
		append_areas(i)
	for i in range(0, num_rectangles):
		print(f"Rectangle #{i+1} area: {rectangle_areas[i]}")
	print(f"Total rectangle areas: {math.fsum(rectangle_areas)}")

main()

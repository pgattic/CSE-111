from datetime import datetime
import math


width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))


def calculate_volume(w, a, d):
	return (math.pi * (w**2)* a * (w*a + (2540 * d)))/10000000000


volume = calculate_volume(width, aspect, diameter)
filename = "volumes.txt"

print(f"The approximate volume is {volume:.2f} liters.")
print(f"Written to file {filename}")


current_date_and_time = datetime.now()


with open(filename, "at") as volumes_file:
	print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}", file=volumes_file)

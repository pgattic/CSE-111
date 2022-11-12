import math

width = float(input("Width of tire in millimeters: "))
ratio = float(input("Aspect ratio of tires: "))
diameter = float(input("Diameter of wheel: "))

volume = (math.pi * width**2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")

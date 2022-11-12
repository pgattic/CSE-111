import math

"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""

pendulum_length1 = float(input("Length of pendulum 1? "))
pendulum_length2 = float(input("Length of pendulum 2? "))
pendulum_length3 = float(input("Length of pendulum 3? "))
pendulum_length4 = float(input("Length of pendulum 4? "))


def calculate_time(length):
    return (2 * math.pi) * math.sqrt(length/9.81)


T1 = calculate_time(pendulum_length1)
print(f"Time (seconds): {T1:.2f}")


T2 = calculate_time(pendulum_length2)
print(f"Time (seconds): {T2:.2f}")


T3 = calculate_time(pendulum_length3)
print(f"Time (seconds): {T3:.2f}")


T4 = calculate_time(pendulum_length4)

print(f"Time (seconds): {T4:.2f}")


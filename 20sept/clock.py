import time

print("Even minute" if time.localtime().tm_min % 2 == 0 else "Odd minute")

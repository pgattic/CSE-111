

def miles_per_gallon(s, e, g):
	return (e-s)/g

def lp100k_from_mpg(mpg):
	return (235.215 / mpg)

def main():
	start = float(input("Start odometer? "))
	end = float(input("End odometer? "))
	gallons = float(input("Gallons used? "))
	mileage = miles_per_gallon(start, end, gallons)
	mileage_k = lp100k_from_mpg(mileage)
	print(f"Mileage: {mileage:.2f} MPG")
	print(f"Mileage: {mileage_k:.2f} liters per 100km")


main()


provinces_flat = open("provinces.txt", "r")
provinces_list = provinces_flat.read().strip().split("\n")

print(provinces_list)

provinces_list.pop(0)
provinces_list.pop()

for i in range(len(provinces_list)):
	if provinces_list[i] == "AB":
		provinces_list[i] = "Alberta"

alberta_count = provinces_list.count("Alberta")
print(f"Alberta occurs {alberta_count} times")
